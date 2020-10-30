class student:
    def __init__(self, rn, nm, marks):
        self.rn = rn
        self.nm = nm
        self.marks = marks

    def __str__(self):
        return "{},{},{}".format(self.rn, self.nm, self.marks)


s1 = student(1, 'swapnil', 100)
s2 = student(2, 'sss', 200)
s3 = student(3, 'waaa', 300)

context = {'ss': [s1], 'ss1': [s2], 'ss2': [s3]}

for k, v in context.items():
    print(v[0].nm)
    print(v[0].marks)
