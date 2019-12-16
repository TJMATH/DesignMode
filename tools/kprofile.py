import os
import cProfile
import pstats

def do_profile(prof_file, sorted_by="tottime"):
    '''
    性能分析装饰器：
        args: 
            prof_file: prof文件名
            sorted_by: 按照指定指标排序
    '''
    def wrapper(func):
        def profiled_func(*args, **kwargs):
            # 获取环境变量，判断是否进行性能分析
            DO_PROF = os.getenv('PROFILING')
            if DO_PROF:
                profile = cProfile.Profile()
                profile.enable()
                result = func(*args, **kwargs)
                profile.disable()
                # 排序
                ps = pstats.Stats(profile).sort_stats(sorted_by)
                ps.dump_stats(prof_file)
            else:
                result = func(*args, **kwargs)
            return result
        return profiled_func
    return wrapper