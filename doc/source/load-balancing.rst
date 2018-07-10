.. _load_balancing_intro:

==========================================
Load Balancing with Percona XtraDB Cluster
==========================================

To provide web servers with an access to the database cluster, one needs a 
TCP load balancer - a lightweight proxy application to be placed between the 
MySQL clients and databse servers. Several solutions can be configured to
perform this task for |PXC|. Among them are ProxySQL_, `HAProxy <http://www.haproxy.org/>`_,
` MariaDB MaxScale <https://mariadb.com/products/technology/maxscale>`_, and 
`MySQl Router <https://www.mysql.com/products/enterprise/router.html>`_ (a
replacement solution for now stalled MySQL Proxy).

Listed proxy applications have different set of features, and therefore are
compatible with |PXC| to different extent. Quick comparison of their features
can be find out from the following table.

  +------------------+----------+-----------+---------+--------------+
  |                  | ProxySQL | MaxScale  | HAProxy | MySQl Router |
  
  |                  |          |           |         |              |
  +------------------+----------+-----------+---------+--------------+
  | License          | GPL v.3  |Proprietary| GPL     |  GPL         |
  +------------------+----------+-----------+---------+--------------+

+------------------+----------+-----------+---------+--------------+
|                  | ProxySQL | MaxScale  | HAProxy | MySQl Router |
+------------------+----------+-----------+---------+--------------+
| License                                                          |
+------------------+----------+-----------+---------+--------------+
| Open Source |
 [(GPL)](https://github.com/sysown/proxysql/blob/master/LICENSE) |
 [(Proprietary)](https://mariadb.com/bsl) |
 [(GPL)](https://www.haproxy.org/download/1.6/doc/LICENSE) |
 [(BSD-2-Clause)](http://nginx.org/LICENSE) |
 [(GPL)](https://github.com/mysql/mysql-router/blob/2.0/License.txt) |
+------------------+----------+-----------+---------+--------------+
| Load balancing |
+------------------+----------+-----------+---------+--------------+
| Application Layer balancer |   |   |
(transport layer only) |
(transport layer only) |
(transport layer only) |
| Weighted Balance |   |   |   |   |   |
+------------------+----------+-----------+---------+--------------+
| Topologies                                                       |
+------------------+----------+-----------+---------+--------------+
| MySQL Master/Slave Replication |   |   |
(external script) |
(external script) |
(very limited) |
| MySQL Group Replication |
(external script) |   |   |   |
(not GA) |
| MySQL NDB Cluster |
(external script) |   |   |   |   |
| Galera Replication |
(external script) |   |
(external sript) |
(external sript) |   |
| Custom membership |
(external script) |   |
(HTTP request) |
(yes commercial) |   |
| Protocols |   |
| MySQL native protocol |   |   |   |   |   |
| MySQL compression |   |   |
(end to end) |
(end to end) |
(end to end) |
| Backend SSL encryption |   |   |
(end to end) |
(end to end) |   |
| Frontend SSL encryption |   |   |
(end to end) |
(end to end) |   |
| Binlog Server |   |   |   |   |   |
| Configuration |   |
| Local config file |   |   |   |   |   |
| Local reconfiguration |   |   |   |   |   |
| Remote reconfiguration |   |   |   |
(yes commercial) |   |
| Zero downtime reconfiguration |   |   |   |   |   |
| Online upgrade (SO\_REUSEPORT) |   |   |   |   |   |
| Connection Management |   |
| Connection Pooling |   |   |   |   |   |
| Backend connections limit |   |   |   |   |   |
| Frontend connections limit |   |   |   |   |   |
| Per user connections limit |   |   |   |   |   |
| Connection Multiplexing |   |   |   |   |   |
| Timeout in millisecond |   |
(seconds only) |   |   |
(seconds only) |
| Persistent Connection |   |
| Transaction tracking |   |   |   |   |   |
| User tracking |   |   |   |   |   |
| Schema tracking |   |   |   |   |   |
| Charset tracking |   |   |   |   |   |
| Session variables tracking |   |   |   |   |   |
| Routing |   |
| Queries read/write split |
(regex) |
(query classifier) |   |   |   |
| Port based routing |   |   |   |   |   |
| Query based routing |
(regex) |   |   |   |   |
| Hint based routing |   |   |   |   |   |
| Sharding |   |
| Schema based sharding |   |   |   |   |   |
| User based sharding |   |   |   |   |   |
| Query based sharding |
(regex) |   |   |   |   |
| Hint based sharding |   |   |   |   |   |
| Queries management |   |
| Rewrite |   |   |   |   |   |
| Recursive rewrite |   |   |   |   |   |
| Timeout |   |   |   |   |   |
| Retry on failure |   |   |   |   |   |
| Throttling |   |
| Query Throttling |   |   |   |   |   |
| Security |   |
| Firewall |   |   |   |   |   |
| Data Masking |   |   |   |   |   |
| Mirroring |   |
| Query mirroring |   |   |   |   |   |
| Query rewrite |   |   |   |   |   |
| Mirror statistics |   |   |   |   |   |
| Query Caching |   |
| Caching by query |   |   |   |   |   |
| Caching by user |   |   |   |   |   |
| Caching by schema |   |   |   |   |   |
| Caching by hint |   |   |   |   |   |
| Prepared statements |   |
| General PS support |   |   |   |   |   |
| PS metadata caching |   |   |   |   |   |
| PS reuse |   |   |   |   |   |
| Logging |   |
| All queries logging |   |   |   |   |   |
| JSON format |   |   |   |   |   |
| Streaming to Kafka |   |   |   |   |   |
| Export metrics |   |
| Locally |   |
(limited) |
(Network related) |
(Network related) |   |
| Remotely |   |   |
(Network related) |
(Network related) |   |
| Queryable |
(Using SQL) |   |   |   |   |
| Export to monitoring/trending tools
(graphite/prometheus/others) |   |   |   |   |   |
| Queries response time |   |
(Top queries) |   |   |   |
| Queries digests |   |


