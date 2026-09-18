class Solution {
    public int numIslands(char[][] grid) {
        int count=0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[i].length;j++){
                if(isValid(i,j,grid,visited)){ 
                    System.out.println(count);
                    System.out.println(i);
                    System.out.println(j);
                    System.out.println(Arrays.deepToString(visited));
                    count+=1;
                    dfs(i,j,grid,visited);
                }
            }
        }
        return count;
    }

    public void dfs(int i,int j,char[][] grid,boolean[][] visited){
        visited[i][j]=true; 
        if(isValid(i+1,j,grid,visited)){
            dfs(i+1,j,grid,visited);
        }
        if(isValid(i,j+1,grid,visited)){
            dfs(i,j+1,grid,visited);
        }
        if(isValid(i-1,j,grid,visited)){
            dfs(i-1,j,grid,visited);
        }
        if(isValid(i,j-1,grid,visited)){
            dfs(i,j-1,grid,visited);
        }
    }
   public boolean isValid(int i,int j , char[][] grid,boolean[][] visited){
    if(i<0 || j<0 || i>= grid.length || j>=grid[0].length){
       return false;
    }
    if(visited[i][j]){
        return false;
    }
    
    if(grid[i][j]=='0'){
        return false;
    }
    return true;
   }
}
