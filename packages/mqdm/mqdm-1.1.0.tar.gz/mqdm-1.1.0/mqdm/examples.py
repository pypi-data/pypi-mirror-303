import time
import mqdm as M
from mqdm import mqdm, pool, print


# ---------------------------------------------------------------------------- #
#                                   Examples                                   #
# ---------------------------------------------------------------------------- #


def example_group():
    t0 = time.time()
    for i in range(10):
        for j in mqdm(range(100), desc=f'blah {i}'):
            time.sleep(0.005)
        print("loop")
    print(f"done in {time.time() - t0:.2f} seconds")

    t0 = time.time()
    with M.group():
        for i in range(10):
            for j in mqdm(range(100), desc=f'blah {i}'):
                time.sleep(0.005)
            print("loop")
    print(f"done in {time.time() - t0:.2f} seconds")

    t0 = time.time()
    for i in range(10):
        for j in mqdm(range(100), desc=f'blah {i}'):
            time.sleep(0.005)
        print("loop")
    print(f"done in {time.time() - t0:.2f} seconds")



def example_bar(n=8, sleep=1, transient=False, error=False, indet=False, embed=False, bp=False):
    t0 = time.time()
    xs = range(n)
    if indet:
        xs = (x for x in xs)
    for i in M.mqdm(xs, desc='example', transient=transient):
        M.set_description(f'example {i}')
        for j in M.mqdm(range(10), desc=f'blah {i}', transient=transient):
            time.sleep(0.04 * sleep)
            if j == 5 and not i % 2:
                # print("blah", i, j)
                if error: 1/0
                if embed: M.embed()
                if bp: M.bp()
    print(f"done in {time.time() - t0:.2f} seconds")


def example_fn(i, error=False, sleep=1):
    import time
    import random
    for i in mqdm(range(i + 1), desc=f'example {i}'):
        t = sleep * random.random()*2 / (i+1)
        time.sleep(t)
        print(i, "slept for", t)
        # mqdm_.set_description("sleeping for %.2f" % t)
        if error: 1/0

def example_pool(n=5, transient=False, n_workers=5, **kw):
    import time
    t0 = time.time()
    pool(
        example_fn,
        # example_bar, 
        range(n), 
        '[bold blue]Very important work',
        bar_kw={'transient': transient},
        # transient=True,
        n_workers=n_workers,
        **kw)
    print("done in", time.time() - t0, "seconds", 123)


def example_messy(n=3, transient=False, n_workers=5, **kw):
    import time
    t0 = time.time()
    example_bar(2, transient=False)
    pbar = mqdm(desc='example leftover', leave=True)
    # pbar1 = mqdm(desc='other', total=10)
    # with pbar:
    pbar.update()
    # time.sleep(1)
    pbar.update()
    # time.sleep(1)
    # pbar.__enter__()
    pbar.update()

    pool(
        example_fn, 
        range(n), 
        '[bold blue]Very important work',
        bar_kw={'transient': True},
        n_workers=n_workers,
        **kw)
    pbar.update()
    pbar.update()
    time.sleep(1)
    example_bar(3, sleep=1, transient=True)
    time.sleep(1)
    pbar.update(total=3)
    # pbar.__exit__(None, None, None)
    # time.sleep(1)
    # mqdm_.pbar.remove_task(0)
    # mqdm_.pbar.stop()
    # time.sleep(1)
    # example(2, transient=False)
    print("done in", time.time() - t0, "seconds", 123)
    pbar.close()
    # M.pbar.stop()
    # time.sleep(1)
    print("done in", time.time() - t0, "seconds", 123)
    print("done in", time.time() - t0, "seconds", 123)
    # print("done in", time.time() - t0, "seconds", 123)
    # print("done in", time.time() - t0, "seconds", 123)
    # print("done in", time.time() - t0, "seconds", 123)
    # print("done in", time.time() - t0, "seconds", 123)
    # 1/0

    # example_bar(2, transient=False)
    # M.pbar.stop()