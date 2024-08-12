import logging
import random
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s] %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)


class Nimmt:
    def __init__(self, *players) -> None:
        self.num = len(players)

        self.players = list(players)

    def game_setting(self):
        self._this_game_cards = random.sample(list(range(1, 105)), self.num * 10 + 4)

        self.board = sorted([[self._this_game_cards.pop()] for _ in range(4)])

        for idx, x in enumerate(self.players):
            x.receive_hand(self._this_game_cards[idx * 10 : (idx + 1) * 10])

        self.play_area = [0] * self.num

        for x in self.players:
            x.bullhead_stack = []

        self.cards_counter = [0] * 104
        for x in self.play_area:
            self.cards_counter[x - 1] += 1

    def play(self):
        logging.debug(f"players are {[x.name for x in self.players]}")
        logging.debug("Start")
        game_cnt = 1
        flg = True
        for x in self.players:
            x.past_scores = []

        while flg:
            logging.debug(f"[Start] Game{game_cnt}")
            self.game_setting()
            for turn in range(1, 11):
                logging.debug(f"{game_cnt=} {turn=} Start")
                for x in self.board:
                    logging.debug(x)

                for i in range(self.num):
                    self._call_submit_card(i)

                    if self.play_area.count(0) == 0:
                        logging.debug("[Open]")
                        self._open()

                        for x in self.players:
                            x.print_result(
                                f"Player: {x.name.ljust(7)}, "
                                + f"Score:{str(x.calc_this_game_score()).rjust(3)}, "
                                + f"Stack: {x.get_fromatted_stack_string()}"
                            )

            logging.debug(f"[End] Game{game_cnt}")
            game_cnt += 1
            result_scores = []
            for i in range(self.num):
                this_game_score = self.players[i].calc_this_game_score()
                self.players[i].past_scores.append(this_game_score)
                score_sum = sum(self.players[i].past_scores)
                result_scores.append(score_sum)
                if score_sum >= 66:
                    flg = False
                    logging.debug(
                        f"Player: {self.players[i].name.ljust(7)} ScoreSum:{str(score_sum).rjust(3)} :Loser"
                    )
                else:
                    logging.debug(
                        f"Player: {self.players[i].name.ljust(7)} ScoreSum:{str(score_sum).rjust(3)}"
                    )
        return result_scores

    def _open(self):
        for _ in range(self.num):
            target_player = self.play_area.index(min(self.play_area))
            tmp_card = self.play_area[target_player]

            self.cards_counter[tmp_card - 1] += 1

            logging.debug(
                f"Player: {self.players[target_player].name.ljust(7)} Card: {str(tmp_card).rjust(3)}"
            )

            idx, val = self._find_adjacent_row(self.board, tmp_card)

            if val == 0:
                logging.debug(
                    f"{self.players[target_player].name.ljust(7)}のカードは置けない！"
                )
                selected_row = self.players[target_player].select_row(self.board)
                logging.debug(f"{selected_row+1}行目を回収した")
                self.players[target_player].pickup_row(self.board[selected_row])
                self.board[selected_row] = [tmp_card]

            else:
                selected_row = idx
                if len(self.board[selected_row]) == 5:
                    self.players[target_player].pickup_row(self.board[selected_row])
                    self.board[selected_row] = [tmp_card]
                    logging.debug(
                        f"{self.players[target_player].name.ljust(7)}のカードは6枚目だ！"
                    )
                    logging.debug(f"{selected_row+1}行目を回収した")
                else:
                    self.board[selected_row].append(tmp_card)
                    logging.debug(
                        f"{self.players[target_player].name.ljust(7)}は{selected_row+1}行目に置いて無事だった"
                    )
            self.play_area[target_player] = 105
            time.sleep(0)
        self.play_area = [0] * self.num

    def _call_submit_card(self, player_num):
        card = self.players[player_num].submit_card(self.board, self.cards_counter)

        self.play_area[player_num] += card

    def _find_adjacent_row(self, board, card):
        idx = 5
        val = 0

        for i in range(4):
            if val < board[i][-1] < card:
                val = board[i][-1]
                idx = i

        return idx, val


class RandomPlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bullhead_stack = []
        self.past_scores = []

    def get_fromatted_hand_string(self):
        return "[" + ", ".join([f"{str(card).rjust(3)}" for card in self.hand]) + "]"

    def get_fromatted_stack_string(self):
        return (
            "["
            + ", ".join([f"{str(card).rjust(3)}" for card in self.bullhead_stack])
            + "]"
        )

    def receive_hand(self, cards):
        self.hand.extend(cards)
        self.hand.sort()

    def pick_up_row(self, cards):
        self.bullhead_stack.extend(cards)

    def submit_card(self, board, counter):
        selected = random.choice(self.hand)
        self.hand.remove(selected)
        return selected

    def select_row(self, board):
        return random.choice([0, 1, 2, 3])

    def pickup_row(self, cards):
        self.bullhead_stack.extend(cards)
        return

    def calc_each_rows_score(self, board):
        return [sum(x) for x in board]

    def calc_this_game_score(self):
        tmp = 0
        for x in self.bullhead_stack:
            if x == 55:
                tmp += 7
            elif x % 11 == 0:
                tmp += 5
            elif x % 10 == 0:
                tmp += 3
            elif x % 5 == 0:
                tmp += 2
            else:
                tmp += 1
        return tmp

    def print_result(self, res):
        pass


class MinPlayer(RandomPlayer):
    def select_row(self, board):
        rows_score = self.calc_each_rows_score(board)
        min_row_value = min(rows_score)
        if rows_score.count(min_row_value) == 1:
            return rows_score.index(min_row_value)
        else:
            return random.choice(
                [idx for idx, x in enumerate(rows_score) if x == min_row_value]
            )

    def submit_card(self, board, counter):
        selected = min(self.hand)
        self.hand.remove(selected)
        return selected


class HumanPlayer(RandomPlayer):
    def __init__(self, name=None):
        if name is None:
            self.name = input("名前を入力してください: ")
        else:
            self.name = name
        self.hand = []
        self.bullhead_stack = []
        self.past_scores = []

    def receive_hand(self, cards):
        self.hand.extend(cards)
        self.hand.sort()
        logging.debug("手札が配られました" + self.get_fromatted_hand_string())

    def submit_card(self, board, counter):
        logging.debug("現在の手札" + self.get_fromatted_hand_string())

        row_info = [[] for _ in range(4)]
        for idx, row in enumerate(board):
            row_info[idx].append(len(row))
            row_info[idx].append(row[-1])
            counter[row[-1]] = -1
            row_info[idx].append(self.calc_cards(*row))

        reset_row = -1
        cnt = 0
        score_cnt = 0
        for i in range(104):
            if counter[i] == -1:
                for j in range(4):
                    if row_info[j][1] == i + 1:
                        row_info[j].append(cnt)
                        row_info[j].append(score_cnt)
                        cnt, score_cnt = 0, 0
                        break
            elif counter[i] == 0:
                cnt += 1
                score_cnt += self.calc_cards(i + 1)

        logging.debug("row_info")
        for x in row_info:
            if len(x) < 5:
                x.extend([[], []])
            logging.debug(
                "列の長さ: {}, 最後の札: {}, 列スコア: {}, 後続カード: {}, 後続スコア: {}".format(
                    *x
                )
            )
        print(counter)

        selected_card = ""
        while not (selected_card.isdecimal()) or int(selected_card) not in self.hand:
            selected_card = input("カードを選択してください: ")

        selected_card = int(selected_card)
        self.hand.remove(selected_card)
        logging.debug(f"selected_card: {selected_card}")
        return selected_card

    def select_row(self, board):
        for idx, x in enumerate(board):
            print(f"Row{idx+1}: {' '.join([str(y).rjust(3) for y in x])}")
        selected_row = ""
        while not (selected_row.isdecimal()) or selected_row not in [
            "1",
            "2",
            "3",
            "4",
        ]:
            selected_row = input("とる列を選んでください: ")
            logging.debug(f"selected_row: {int(selected_row)-1}")
        return int(selected_row) - 1

    def calc_cards(self, *cards):
        tmp = 0
        for x in cards:
            if x == 55:
                tmp += 7
            elif x % 11 == 0:
                tmp += 5
            elif x % 10 == 0:
                tmp += 3
            elif x % 5 == 0:
                tmp += 2
            else:
                tmp += 1
        return tmp

    def pick_up_row(self, cards):
        print(f"{cards}をゲットしました！")
        return super().pick_up_row(cards)

    def print_result(self, res):
        print("[Result]")
        print(res)
        return


def evaluate_players(*players, num_games=1000):
    num = len(players)
    scores = [[] for _ in range(num)]
    win_count = [0] * num

    for i in range(num_games):
        game = Nimmt(*list(players))
        this_game_scores = game.play()
        for i, score in enumerate(this_game_scores):
            scores[i].append(score)
            if score < 66:
                win_count[i] += 1

    avgs = [sum(x) / num_games for x in scores]
    win_rates = [x / num_games for x in win_count]

    for i, avg, win_rate in zip(range(num), avgs, win_rates):
        print(
            f"Player {i+1} - Avg Score: {avg:.3}, Win Rate: {win_rate:.3} {type(players[i])}"
        )


a = MinPlayer("Alice")
b = MinPlayer("Bob")
c = RandomPlayer("Charlie")
d = RandomPlayer("David")
e = HumanPlayer("Emma")
f = RandomPlayer("Frank")
g = RandomPlayer("Grace")
h = RandomPlayer("Hery")
i = RandomPlayer("Isabel")
j = RandomPlayer("Jack")


evaluate_players(a, b, c, d, e, num_games=1)
