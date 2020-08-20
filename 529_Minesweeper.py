class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        h, w = len(board), len(board[0]) 
        cur_y, cur_x = click 
        
        
        def in_range(x, y): 
            
            return  0 <= x < w and 0 <= y < h
        
        
        def offset_to_neighbour(): 
            
            for dx, dy in ((+1,  0), (-1,  0), (  0, +1), (  0,-1), 
                            (+1, +1), (+1, -1), ( -1, +1), ( -1,-1)):
            
                yield (dx, dy) 
                
            
        def has_mine_around(x, y): 
            
            mine_count = 0 
            
            for dx, dy in iter( offset_to_neighbour() ): 
                
                next_x, next_y = (x+dx, y +dy) 
            
                if in_range(next_x, next_y) and board[next_y][next_x] == 'M':
                    mine_count += 1
                
            return mine_count 
        
        
        def dfs(x, y) : 
            
            if not in_range(x, y) or board[y][x] != 'E': 
                return 
            
            
            board[y][x] = '#' 
            
            mine_count = has_mine_around(x, y) 
            
            if not mine_count: 
                
                for dx, dy in iter( offset_to_neighbour() ): 
                    dfs(x + dx, y + dy) 
                    
                    
                board[y][x] = 'B' 
                
                
                
            else: 
                
                board[y][x] = str(mine_count)
            
            return 
        
        if board[cur_y][cur_x] == 'M':
            
            board[cur_y][cur_x] = 'X' 
        
        elif board[cur_y][cur_x] == 'E': 
            
            dfs(cur_x, cur_y) 
            
            
        return board 
            
                
                    
                    
            
        
        
