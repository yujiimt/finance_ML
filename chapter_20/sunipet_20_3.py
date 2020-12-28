import numpy as np

def main():
    # 経路依存性のある処理：順次実行での実装
    r = np.random.normal(0, 0.01, size = (1000, 100000))
    t = barrierTouch(r)
    return 

def barrierTouch(r, width=0.5):
    #最も早いバリアタッチのインデックスを見つける
    t, p = {}, np.log((1+r).cumprod(axis=0))
    for j in xrange(r.shape[1]): #列方向のループ
        for i in xrange(r.shape[0]): # 行方向のループ
            if p[i, j] >= width or p[i, j] <= -width:
                t[j] = i
                continue
    return t


if __name__ == "__main__":
    import timeit
    print(min(timeit.Timer("main0()", setup = "from __main__ import main0").repeat(5, 10)))