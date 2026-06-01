
import sys
import time
from collections import defaultdict, deque

def input(): return sys.stdin.readline().strip()
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())

drct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class RollingHash:
    def __init__(self, S, b=3491, m=999999937):
        n = len(S)
        self.prefix = [0] * (n + 1)
        self.power = [1] * (n + 1)
        self.b = b
        self.m = m
        for i in range(n):
            c = ord(S[i])
            self.prefix[i + 1] = (self.prefix[i] * b + c) % m
            self.power[i + 1] = (self.power[i] * b) % m

    def get(self, left, right):
        return (self.prefix[right] - self.power[right - left] * self.prefix[left]) % self.m

# 解答圧縮関数
def compress_operations_rh(O: str, max_len: int = 50) -> str:
    K = len(O)
    if K < 4: return O
        
    rh = RollingHash(O)
    best_profit = 0
    best_positions = []
    best_L = 0
    best_start = -1
    
    limit = min(max_len, K // 2)
    for L in range(2, limit + 1):
        hash_to_indices = defaultdict(list)
        for i in range(K - L + 1):
            h = rh.get(i, i + L)
            hash_to_indices[h].append(i)
            
        for h, indices in hash_to_indices.items():
            if len(indices) < 2: continue
                
            count = 0
            last_end = -1
            valid_positions = []
            for idx in indices:
                if idx >= last_end:
                    valid_positions.append(idx)
                    count += 1
                    last_end = idx + L
                    
            if count >= 2:
                profit = (L * count) - (L + count + 1)
                if profit > best_profit:
                    best_profit = profit
                    best_positions = valid_positions
                    best_L = L
                    # 修正: リストではなく先頭のインデックス数値を取得する
                    best_start = valid_positions[0]
                    
    if best_profit <= 0: return O
        
    best_sub = O[best_start : best_start + best_L]  # pyright: ignore[reportOperatorIssue]
    res = []
    idx = 0
    pos_idx = 0
    num_pos = len(best_positions)
    
    while idx < K:
        if pos_idx < num_pos and idx == best_positions[pos_idx]:
            if pos_idx == 0:
                res.append("M" + best_sub + "M")
            else:
                res.append("P")
            idx += best_L
            pos_idx += 1
        else:
            res.append(O[idx])
            idx += 1
            
    return "".join(res)

# 状態管理クラス
class State:
    def __init__(self, r, c, d, ops, holding_ball, ball_pos, completed_mask):
        self.r = r           
        self.c = c           
        self.d = d           
        self.ops = ops       
        self.score = 0.0     
        self.holding_ball = holding_ball 
        self.ball_pos = ball_pos 
        self.completed_mask = completed_mask 
        
    def get_key(self):
        return (self.r, self.c, self.d, self.holding_ball, tuple(self.ball_pos), self.completed_mask)

# メインソルバー
class AHC066Solver:
    def __init__(self, N, M, T, v, h, ball_and_box):
        self.N = N
        self.M = M
        self.T = T
        self.v = v
        self.h = h
        self.ball_and_box = ball_and_box
        
        self.dist = self._precompute_dist()
        # 修正: ボールの初期座標 (b, b) を指定
        self.initial_ball_pos = {i: (b[0], b[1]) for i, b in enumerate(ball_and_box)}

    def get_box_pos(self, ball_id):
        # 修正: かごの座標 (2番目と3番目の要素) を指定
        return self.ball_and_box[ball_id][2], self.ball_and_box[ball_id][3]

    def _precompute_dist(self):
        N = self.N
        INF = 10**9
        dist = [[[[INF] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
        
        for r in range(N):
            for c in range(N):
                dist[r][c][r][c] = 0
                q = deque([(r, c)])
                
                while q:
                    cr, cc = q.popleft()
                    d = dist[r][c][cr][cc]
                    
                    if cr + 1 < N and self.h[cr][cc] == '0' and dist[r][c][cr+1][cc] == INF:
                        dist[r][c][cr+1][cc] = d + 1
                        q.append((cr+1, cc))
                    if cr - 1 >= 0 and self.h[cr-1][cc] == '0' and dist[r][c][cr-1][cc] == INF:
                        dist[r][c][cr-1][cc] = d + 1
                        q.append((cr-1, cc))
                    if cc + 1 < N and self.v[cr][cc] == '0' and dist[r][c][cr][cc+1] == INF:
                        dist[r][c][cr][cc+1] = d + 1
                        q.append((cr, cc+1))
                    if cc - 1 >= 0 and self.v[cr][cc-1] == '0' and dist[r][c][cr][cc-1] == INF:
                        dist[r][c][cr][cc-1] = d + 1
                        q.append((cr, cc-1))
        return dist

    def evaluate_state(self, state: State) -> float:
        if state.completed_mask == (1 << self.M) - 1:
            return 1000000.0 

        completed_count = bin(state.completed_mask).count("1")
        score = float(completed_count * 100000)
        
        min_cost = float(10**9)
        
        if state.holding_ball != -1:
            target_box_r, target_box_c = self.get_box_pos(state.holding_ball)
            dist_to_box = self.dist[state.r][state.c][target_box_r][target_box_c]
            min_cost = float(dist_to_box)
            if dist_to_box > 0:
                min_cost += 0.5 
        else:
            for b_id in range(self.M):
                if (state.completed_mask & (1 << b_id)):
                    continue
                    
                b_r, b_c = state.ball_pos[b_id]
                box_r, box_c = self.get_box_pos(b_id)
                
                d_to_ball = self.dist[state.r][state.c][b_r][b_c]
                d_to_box = self.dist[b_r][b_c][box_r][box_c]
                
                cost = d_to_ball + d_to_box
                if cost < min_cost:
                    min_cost = float(cost)

        score -= min_cost
        score -= len(state.ops) * 0.1 
        
        return score

    def can_move_forward(self, r, c, d):
        # 修正: drct[d] と drct[d] で個別の要素を取り出す
        nr, nc = r + drct[d][0], c + drct[d][1]
        if nr < 0 or nr >= self.N or nc < 0 or nc >= self.N: return False
        
        if d == 0: return self.v[r][c] == '0'      # 東
        if d == 1: return self.h[r][c] == '0'      # 南
        if d == 2: return self.v[r][nc] == '0'     # 西
        if d == 3: return self.h[nr][c] == '0'     # 北
        return False

    def solve(self):
        BEAM_WIDTH = 50 
        MAX_DEPTH = self.T 

        initial_state = State(
            r=0, c=0, d=0, ops="", 
            holding_ball=-1, 
            ball_pos=self.initial_ball_pos.copy(), 
            completed_mask=0
        )
        initial_state.score = self.evaluate_state(initial_state)
        current_states = [initial_state]
        
        visited = set()
        visited.add(initial_state.get_key())

        best_final_state = initial_state
        start_time = time.time()

        for depth in range(MAX_DEPTH):
            # 実行時間制限
            if time.time() - start_time > 2.8:
                break
                
            if not current_states:
                break

            next_states = []

            for state in current_states:
                if state.completed_mask == (1 << self.M) - 1:
                    if best_final_state.completed_mask != (1 << self.M) - 1 or len(state.ops) < len(best_final_state.ops):
                        best_final_state = state
                    continue

                # --- 前進 (F) ---
                if self.can_move_forward(state.r, state.c, state.d):
                    # 修正: drct[state.d], drct[state.d]
                    nr, nc = state.r + drct[state.d][0], state.c + drct[state.d][1]
                    ns = State(nr, nc, state.d, state.ops + "F", state.holding_ball, state.ball_pos.copy(), state.completed_mask)
                    if ns.get_key() not in visited:
                        ns.score = self.evaluate_state(ns)
                        visited.add(ns.get_key())
                        next_states.append(ns)
                
                # --- 右折 (R) ---
                ns_r = State(state.r, state.c, (state.d + 1) % 4, state.ops + "R", state.holding_ball, state.ball_pos.copy(), state.completed_mask)
                if ns_r.get_key() not in visited:
                    ns_r.score = self.evaluate_state(ns_r)
                    visited.add(ns_r.get_key())
                    next_states.append(ns_r)

                # --- 左折 (L) ---
                ns_l = State(state.r, state.c, (state.d - 1) % 4, state.ops + "L", state.holding_ball, state.ball_pos.copy(), state.completed_mask)
                if ns_l.get_key() not in visited:
                    ns_l.score = self.evaluate_state(ns_l)
                    visited.add(ns_l.get_key())
                    next_states.append(ns_l)

                # --- 交換 (S) ---
                ground_ball = -1
                is_completed_ball_here = False
                for b_id in range(self.M):
                    if state.ball_pos[b_id] == (state.r, state.c):
                        ground_ball = b_id
                        if (state.completed_mask & (1 << b_id)):
                            is_completed_ball_here = True
                        break

                if not is_completed_ball_here:
                    if state.holding_ball == -1 and ground_ball != -1:
                        new_ball_pos = state.ball_pos.copy()
                        new_ball_pos[ground_ball] = (-1, -1)
                        ns_s = State(state.r, state.c, state.d, state.ops + "S", ground_ball, new_ball_pos, state.completed_mask)
                        if ns_s.get_key() not in visited:
                            ns_s.score = self.evaluate_state(ns_s)
                            visited.add(ns_s.get_key())
                            next_states.append(ns_s)

                    elif state.holding_ball != -1:
                        h_ball = state.holding_ball
                        new_ball_pos = state.ball_pos.copy()
                        new_mask = state.completed_mask
                        
                        new_ball_pos[h_ball] = (state.r, state.c)
                        box_r, box_c = self.get_box_pos(h_ball)
                        
                        if state.r == box_r and state.c == box_c:
                            new_mask |= (1 << h_ball)
                            
                        new_holding = ground_ball
                        if ground_ball != -1:
                            new_ball_pos[ground_ball] = (-1, -1) 
                            
                        ns_s = State(state.r, state.c, state.d, state.ops + "S", new_holding, new_ball_pos, new_mask)
                        if ns_s.get_key() not in visited:
                            ns_s.score = self.evaluate_state(ns_s)
                            visited.add(ns_s.get_key())
                            next_states.append(ns_s)

            if not next_states:
                break
                
            next_states.sort(key=lambda s: s.score, reverse=True)
            current_states = next_states[:BEAM_WIDTH]
            
            if current_states:
                is_best_completed = (best_final_state.completed_mask == (1 << self.M) - 1)
                if (not is_best_completed) and current_states[0].score > best_final_state.score:
                    best_final_state = current_states[0]

        best_operations = best_final_state.ops
        # 最後になるべく解答を圧縮する
        compressed_operations = compress_operations_rh(best_operations)
        
        for op in compressed_operations:
            print(op)

def main():
    N, M, T = i_map()
    v = [input() for _ in range(N)]
    h = [input() for _ in range(N-1)]
    ball_and_box = [i_list() for _ in range(M)]

    solver = AHC066Solver(N, M, T, v, h, ball_and_box)
    solver.solve()

if __name__ == "__main__":
    main()
