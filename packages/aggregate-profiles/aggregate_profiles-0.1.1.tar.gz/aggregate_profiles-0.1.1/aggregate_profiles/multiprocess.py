import multiprocessing

def exec_mlproc_function(target, func, *args):
    """ execute function over targer thru multiple processes, store result in a list """
    output_list = []
    # process pool
    with multiprocessing.Pool() as pool:
        # EXECUTE asynchronously the application of 
        results = [pool.apply_async(func, (targ,*args)) for targ in target]

        # Get the results
        for result in results:
            output_list.append(result.get())

    return output_list
    