import ConfigParser
import io

sample_config = """
[mysqld]
user = mysql
pid-file = /var/run/mysqld/mysqld.pid
skip-external-locking
old_passwords = 1
skip-bhd
skip-innodb
"""

config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

#Settings with values are treated as before:
config.get("mysqld", "user")
