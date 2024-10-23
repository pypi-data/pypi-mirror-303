from docketpy.python import PythonTask, PythonVirtualEnvTask

def say_hello():
    print("Hello, world!")


def print_numpy_with_name(name):
    print(f"Printing np.__version__: {np.__version__}, name: {name}") 
    return f"np.__version__:{np.__version__}, name: {name}"


pt = PythonTask(callable = say_hello)
pt.run()

pv_t1 = PythonVirtualEnvTask(callable=say_hello, requirements=["numpy", "pandas", "redis", "google-cloud-storage", "dill"]).run()
print(pv_t1)
pv_t2 = PythonVirtualEnvTask(
    callable=print_numpy_with_name, 
    show_return_value_in_logs=True, 
    requirements=["numpy", "pandas", "redis", "google-cloud-storage", "dill"], 
    op_kwargs={"name": "xyz"}
    ).run()
print(pv_t2)

# def say_hi():
#     print(f"__file__: {__file__}")
#     print(os.path.abspath(__file__))
#     print(os.path.dirname(__file__))
#     print(os.path.basename(__file__))
#     print(os.path.basename(__file__).rstrip(".py"))
#     say_hi_for_name("abc")


# def get_numpy_version():
#     print("abc")
#     print(f"printing np.__version__: {np.__version__}") 
#     return (np.__version__)



# def say_hi_for_name(name = "world"):
#     return print(f"Hello {name}!")


# def say_hi():
#     print("Hello, world!")


# def say_hi_for_name(name):
#     print(f"Print Name: {name}!")
#     return f"Name: {name}!"


# def say_hi_with_time():
#     print(f"Hello, India! It's {datetime.now()}\n")
#     print(f"Hello, World! It's {datetime.now()}\n")
#     print(f"Hello, Earth! It's {datetime.now()}\n")
#     print(f"Hello, Universe! It's {datetime.now()}\n")
#     return "Hello, Hello!"


# def long_task_with_logs(n:int):
#     for i in range(n):
#         print(f"Long task running: {i}")
#         time.sleep(2)
#     return "Long task done!"


# def say_hi_with_time():
#     print(f"Hello, India! It's {datetime.now()}\n")
#     print(f"Hello, World! It's {datetime.now()}\n")
#     print(f"Hello, Earth! It's {datetime.now()}\n")
#     print(f"Hello, Universe! It's {datetime.now()}\n")
#     return "Hello, Hello!"


# def get_numpy_version():
#     print(np.__version__) 

# # say_hi()
# # say_hi_with_time()
# # print(get_numpy_version())

# # pt = PythonTask(callable = say_hi)
# # pt.run()
# # pt = PythonTask(callable = say_hi_for_name, name = "Docket", show_return_value_in_logs = True)
# # pt.run()

# # PythonTask(callable = say_hi_with_time, show_return_value_in_logs = True).run()
# # PythonTask(callable = long_task_with_logs, show_return_value_in_logs = True, n=2).run()
# # # PythonTask(callable = get_numpy_version, kw_args = {}).run()    

# # x = PythonTask(callable = get_numpy_version, ).run()
# # print(x)

# # x = PythonVirtualEnvTask(callable=say_hello, requirements=["numpy", "pandas", "redis", "google-cloud-storage", "dill"]).run()
# # print(x)
# # y = PythonVirtualEnvTask(
# #     callable=print_numpy_with_name, 
# #     show_return_value_in_logs=True, 
# #     requirements=["numpy", "pandas", "redis", "google-cloud-storage", "dill"], 
# #     op_kwargs={"name": "xyz"}
# #     ).run()
# # print(y)
