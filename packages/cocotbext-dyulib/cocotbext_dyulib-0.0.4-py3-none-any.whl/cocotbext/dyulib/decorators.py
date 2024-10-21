import cocotb
def printio(func):
    '''
    Function decorator which prints the ingress and egress from a function.
    This is useful for debug as it gives a trace of which functions were called.
    usage:
    @printio
    def fn(...)
    '''
    async def inner(*args, **kwargs):
        cocotb.log.info(f"Enter {func.__name__}")
        await func(*args, **kwargs)
        cocotb.log.info(f"Exit {func.__name__}")
        return inner
