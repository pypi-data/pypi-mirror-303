

import jpype 
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Semaphore
import pkg_resources
from jinja2 import Template

# 全局变量存储 JAR 文件路径
JAR_FILES = [pkg_resources.resource_filename('xcloudforlinux', f'resources/{jar_name}') for jar_name in [
    'XCloudJDBC-2.10.6.7.jar', 'slf4j-api-1.7.5.jar', 'slf4j-log4j12-1.7.5.jar', 
    'slf4j-simple-1.7.5.jar', 'log4j-1.2.17.jar', 'libthrift-0.9.2.jar', 
    'XCloudJDBC_SP_Procedure_Parser-0.1.3.jar', 'lz4-1.3.0.jar'
]]

# 启动 JVM
def start_jvm():
    if not jpype.isJVMStarted():
    # 构建类路径
        jpype.startJVM(classpath=JAR_FILES)
        jpype.JClass('com.bonc.xcloud.jdbc.XCloudDriver')
        print('JVM 启动成功')

def shutdown_jvm():
    if jpype.isJVMStarted():
        jpype.shutdownJVM()
        print('JVM 已关闭')

class DatabaseClient:
    def __init__(self, ip, username, password,max_cursors = 10,if_header_included = False):
        print("Database 开始初始化")
        self.ip = ip
        self.username = username
        self.password = password
        self.connection = self.get_connection()
        self.cursor_semaphore = Semaphore(max_cursors)
        self.executor = ThreadPoolExecutor(max_workers=max_cursors)
        self.futures = []
        self.if_header_included = if_header_included
    def __enter__(self):
        return self  # 返回实例本身，使得可以在with语句中使用
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()
    def get_connection(self):
        try:
            print('开始数据连接')
            DriverManager = jpype.JClass('java.sql.DriverManager')
            print('jdbc加载完成')
            url = f'jdbc:xcloud:@{self.ip}/SERVER_DATA?connectRetry=3&socketTimeOut=43200000&connectDirect=true&buffMemory=33554432'
            print('完成数据库链接')
            return DriverManager.getConnection(url, self.username, self.password)
        except Exception as e:
            print(f"Failed to connect to {self.ip}: {str(e)}")
            raise e
    def execute_query(self, query):
        with self.cursor_semaphore:
            future = self.executor.submit(self.run_query, query)
            self.futures.append(future)
            return future
    def execute_queries(self, queries):
        #with self.cursor_semaphore:  # 控制游标数量
            #for query in queries:
                #self.execute_query(query)  # 使用之前定义的方法提交查询
            #return [future.result() for future in self.futures]
        print('开始客户端查询')
        with self.cursor_semaphore:  # 控制游标数量
            future_to_index = {}
            results = [None] * len(queries)  # 初始化结果列表为 None，长度与查询列表相同

            for i, query in enumerate(queries):
                future = self.executor.submit(self.run_query, query)
                self.futures.append(future)
                future_to_index[future] = i  # 将 future 与其对应的查询索引相关联

            for future in self.futures:
                index = future_to_index[future]  # 获取原始查询的索引
                try:
                    results[index] = future.result()  # 将结果放置在正确的位置
                except Exception as e:
                    results[index] = None  # 处理可能的异常
                    print(f"Error processing query at index {index}: {e}")
                    raise e

            print('客户端查询完成')
            return results

    def run_query(self, query):
        results = []
        if self.connection:
            try:
                print("开始查询")
                statement = self.connection.createStatement()
                resultSet = statement.executeQuery(query)
                metadata = resultSet.getMetaData()
                numColumns = metadata.getColumnCount()
                print("部分已经完成")
                if self.if_header_included:
                    header = [metadata.getColumnName(i) for i in range(1,numColumns + 1)]
                    results.append(tuple(header))
                while resultSet.next():
                    row = [resultSet.getObject(i) for i in range(1,numColumns + 1)]
                    results.append(tuple(row))
            except Exception as e:
                print(f"Error executing query on {self.ip}: {str(e)}")
                raise e
        return results
    def close_connection(self):
        self.executor.shutdown(wait=True)
        if self.connection:
            self.connection.close()
            self.connection = None

def run_query_in_process(ip, username, password, queries,max_cursors = 10,if_header_included = False):
    print('ClientManagement运行查询')
    with DatabaseClient(ip, username, password, max_cursors,if_header_included) as client:
        return client.execute_queries(queries)  # 修改为接收一个查询列表

class ClientManager:
    def __init__(self, client_configs, max_cursors=10):
        self.start_jvm()
        self.client_configs = client_configs
        self.max_cursors = max_cursors
        self.process_pool = ThreadPoolExecutor(max_workers=len(client_configs))
    def __enter__(self):
        return self
    def start_jvm(self):
        if not jpype.isJVMStarted():
            start_jvm()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if jpype.isJVMStarted():
            shutdown_jvm()
    def execute_queries(self, queries, if_header_included = False):
        # 确定根据查询数量动态调整启动的客户端数量
        num_queries = len(queries)
        if num_queries < self.max_cursors:
            num_clients = 1
        else:
            num_clients = min(len(self.client_configs), self.max_cursors)
        
        # 使用ThreadPoolExecutor动态创建线程池
        with ThreadPoolExecutor(max_workers=num_clients) as executor:
            print(JAR_FILES)
            print(f"客户端个数为{num_clients}")  # 打印每个查询返回的结果
            queries_per_client = [queries[i::num_clients] for i in range(num_clients)]
            futures = []
            index_to_result = [None] * num_queries  # 创建与 queries 等长的结果列表，初始化为 None
            # 分发查询到各个客户端
            for i, (config, query_set) in enumerate(zip(self.client_configs, queries_per_client)):
                future = executor.submit(run_query_in_process, config['ip'], config['username'], config['password'], query_set, self.max_cursors,if_header_included)
                start_index = i
                step = num_clients
                futures.append((future, start_index, step))  # 保存每个 future 以及其对应查询的开始索引和步长

            # 收集结果并按原始顺序存放
            for future, start_index, step in futures:
                try:
                    result_set = future.result()
                    for offset, result in enumerate(result_set):
                        index_to_result[start_index + offset * step] = result
                except Exception as e:
                    print(f"Error retrieving results: {e}")
                    raise e
            # 过滤掉 None 值，如果有的话
            if len(index_to_result) != len(queries):
                raise Exception("过程查询出了问题")
            else:
                return index_to_result
    @staticmethod
    def read_multi_sql_file(file_path,**kwargs):
        """
        Read a SQL file containing multiple scripts separated by semicolons,
        apply variable substitution if provided, and return a list of the scripts.
        """
        # Read SQL file
        with open(file_path, 'r', encoding='utf-8') as file:
            sql_content = file.read()
        # Apply variable substitution using Jinja2 template if variables are provided
        if 'variables' in kwargs:
            template = Template(sql_content)
            rendered_content = template.render(kwargs['variables'])
        else:
            rendered_content = sql_content
        # Split SQL scripts by semicolon and remove empty strings
        sql_scripts = [script.strip() for script in rendered_content.split('\n;') if script.strip()]
        return sql_scripts 




