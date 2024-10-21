pre_sign ="!!! ----- >> "
post_sign=" << ----- !!!"
finished_message ="FINISHED"
started_message = "STARTED"

def finish(operation_name):
    print('\n'+pre_sign+ operation_name.upper())
    print(pre_sign+ finished_message)

def start(operation_name):
    print('\n'+pre_sign+ operation_name.upper())
    print(pre_sign+ started_message)
