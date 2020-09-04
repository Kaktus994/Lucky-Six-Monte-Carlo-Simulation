import random

class LuckySix:

	drum = []
	slot_multipiyers_dict = {5:10000, 6:7500, 7:5000, 8:2500, 9:1000, 10:500, 11:300, 12:200, 13:150, 14:100,
						15:90, 16:80, 17:70, 18:60, 19:50, 20:40, 21:30, 22:25, 23:20, 24:15, 25:10, 26:9, 27:8, 28:7, 29:6, 30:5,
						31:4, 32:3, 33:2, 34:1}

	def __init__(self, combination):
		self.combination = combination
		self.round_id = 0
		self.round_numbers = {}

	def set_drum(self):
		self.drum = [i for i in range(1, 49)]

	def new_draw(self):
		self.set_drum()
		for i in range(35):
			self.round_numbers[i] = random.choice(self.drum)
			self.drum.remove(self.round_numbers[i])

	def win(self):

		win_keys = []
		win_combo = all(number in self.round_numbers.values() for number in self.combination)

		if win_combo:
			for key, number in self.round_numbers.items():
				if number in self.combination:
					win_keys.append(key)
			winning = self.slot_multipiyers_dict[max(win_keys)]
			return winning
		else:
			return False

	def get_round_numbers(self):
		return self.round_numbers


"""
Test
"""
if __name__ == "__main__":

	lucky = LuckySix([1, 2, 3, 4 ,5 ,6])

	number_of_rounds = 100
	rounds_won = 0

	for _ in range(number_of_rounds):
		lucky.new_draw()
		winnings = lucky.win()
		if winnings:
			rounds_won += winnings

	print(rounds_won / number_of_rounds)