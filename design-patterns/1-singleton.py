# Restricts the instantioation of a class to only one instance
# this class can only have one single instance
# This is useful when exactly one object is needed to coordinate actions across the entire system

# this example is not the only implementation of Singleton Design Pattern

def singleton(class_instance):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_instance not in instances:     # this will ensure only the called instance will be created
            instances[class_instance] = class_instance(*args, **kwargs)

        return instances[class_instance]

    return get_instance


@singleton      # decorator
class MongoDBConnection():
    def __init__(self) -> None:
        print("DB initialized")

# Review: Decorators are used to change extend the functionality of a function without actually changing the function itself

if __name__ == '__main__':
    mongo_conn_1 = MongoDBConnection()
    mongo_conn_2 = MongoDBConnection()
    # ^ this will create 2 different instances

    print(mongo_conn_1 == mongo_conn_2)

