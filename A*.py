from pymaze import maze,COLOR,agent

def DFS(m):
    dfs_path={}
    start=(5,8)
    explored=[start]
    fountieer=[start]
    while fountieer:
        currCell=fountieer.pop()
        if currCell==():
            break
        for d in "ESWN":
            if m.maze_map[currCell][d]==True:
                if d=="E":
                    childCell=(currCell[0],currCell[1]+1)
                elif d=="W":
                    childCell=(currCell[0],currCell[1]-1)
                elif d=="N":
                    childCell=(currCell[0]-1,currCell[1])
                elif d=="S":
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                fountieer.append(childCell)
                dfs_path[childCell]=currCell
    fw_path={}
    cell=(1,1)
    while cell!=start:
        fw_path[dfs_path[cell]]=cell
        cell=dfs_path[cell]
    return fw_path

m=maze(15,15)
m.CreateMaze(2,8,loopPercent=50)
path=DFS(m)
a=agent(m,4,8,footprints=True)
m.tracePath({a:path})
m.run()

