行云数据库python 驱动JDBC。主要供中国电信、中国移动等通信公司或国家电网等使用国信行云数据库公司使用.
# xcloudClients

## 概述

`xcloudClients` 是一个设计用于通过 JPype 使用 JDBC 在 XCloud 系统上进行数据库操作的 Python 包。它可以高效地管理数据库连接，并利用预配置的客户端实例池来进行并发数据库访问，从而实现 SQL 查询的线程安全执行。

## 特性

- **线程安全的数据库连接**：在多线程中安全管理并发数据库操作。
- **连接池管理**：限制同时打开的数据库游标数量，防止系统过载。
- **异步查询执行**：利用 Python 的 `concurrent.futures` 异步执行查询。
- **资源管理**：自动管理 JDBC 资源并确保正确关闭 JVM 和数据库连接。
- **错误处理**：强大的错误处理能力，能够处理数据库连接问题和 SQL 执行错误。

## 安装

要安装 `xcloudClients`，需要 Python 3.6 或更高版本。您可以直接通过 pip 从 PyPI 安装：

```bash
pip install xcloudClients
 先决条件
 在安装包之前，请确保已经安装并正确配置了 JPype，因为它是 JDBC 连接所必需的。如果还未安装，可以使用 pip 安装 JPype：


```bash
pip install JPype1

## 先决条件
## 在安装包之前，请确保已经安装并正确配置了 JPype，因为它是 JDBC 连接所必需的。如果还未安装，可以使用 pip 安装 JPype：

```bash

pip install JPype1
## 使用方法
## 这里是一个简单的示例，演示如何使用 xcloudClients 来管理数据库连接和执行查询：

## 设置数据库客户端
## 首先，配置数据库客户端设置：

```python
from xcloudClients import ClientManager

# 定义客户端配置
client_configs = [
    {'ip': '192.168.1.100', 'username': 'admin', 'password': 'secret'}
]

# 使用配置初始化 ClientManager
manager = ClientManager(client_configs=client_configs, max_cursors=10)
执行查询
您可以通过从 SQL 文件读取查询，并使用 ClientManager 来执行它们：

```python
# SQL文件的路径
sql_file_path = 'path/to/your/queries.sql'

# 从文件读取 SQL 查询
queries = manager.read_multi_sql_file(sql_file_path)

# 执行查询并检索结果
results = manager.execute_queries(queries, if_header_included=True)
for result in results:
    print(result)


贡献
欢迎对 xcloudClients 做出贡献！请随意 fork 仓库，进行您的更改，并提交 pull 请求。