# __main__.py
from wavefront_package.wavefront_5_pac import Voronoi  # ここで必要なモジュールをインポート
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

def main():
    # コマンドライン引数を処理する場合
    if len(sys.argv) < 2:
        print("Usage: python -m wavefront_package [arguments]")
        vor = Voronoi(500,500) #画像の大きさの指定
        vor.file_input('circle.csv') #入力ファイル指定
        diagram = vor.voronoi_tessellation()
        E,Em,V,Vm = vor.extractEandV(diagram)
        maze = np.zeros((vor.H,vor.W),np.uint8)
        for x,y in E:
            maze[y,x] = 1
        path = vor.search_path(maze,(200,180),(273,320),8)
        plt.figure()
        plt.imshow(maze, cmap=ListedColormap(['white','black','red','gray']))
        for y in range(maze.shape[0]):
            for x in range(maze.shape[1]):
                if maze[y,x] == 1:
                    plt.scatter(x,y,color='black', s= 3)
                elif maze[y,x] == 4:
                    plt.scatter(x,y,color='red',s=4)
        plt.show()
    else:    
        print("Arguments provided: ", sys.argv[1:])

if __name__ == "__main__":
    main()