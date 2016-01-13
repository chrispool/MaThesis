import sys
from random import randint


class Quiz:

	def __init__(self, qFile):
		self.questions = self.readQuestionFile(qFile)
		self.answerQuestions()

	def readQuestionFile(self, qFile):
		result = []
		with open(qFile, encoding='utf-8') as f: 
			for line in f:
				elements = line.split('\t')
				result.append(elements)
		return result

	def answerQuestions(self):
		answers = ["A", "B", "C", "D"]
		cor = 0
		i = 0
		for qId, question, correct, a, b, c, d in self.questions:
			if answers[randint(0,3)] == correct:
				cor += 1
			i +=1

		print(cor/i)
			# print()
			# print(question)
			# print(a)
			# print(b)
			# print(c)
			# print(d)
			# input()
			# print(correct)


quiz = Quiz(sys.argv[1])