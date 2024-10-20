import pybpsapi
import time

group = pybpsapi.CircularCheckerGroup()
mysql_config = {'user': 'u150_VRwcaEHywr', 'password': 'ow+QY6LbU4I.JNakXW3L!dW!', 'host': 'oracleone.nodes.rajtech.me', 'database': 's150_circularbot', 'port': '3306', 'raise_on_warnings': False}

circular_checkers = [
                pybpsapi.CircularChecker(
                    cat, cache_method='mysql',
                    db_name=mysql_config['database'],
                    db_table='cache',
                    db_port=mysql_config['port'],
                    db_password=mysql_config['password'],
                    db_host=mysql_config['host'],
                    db_user=mysql_config['user'],
                ) for cat in ['general', 'ptm', 'exam']
            ]

for checker in circular_checkers:
    group.add(checker)
print("f")
new_circular_objects = group.check()

print(new_circular_objects)
print("new")

# new_circular_objects = group.check()
#
# print(new_circular_objects)
#
# print('new2')