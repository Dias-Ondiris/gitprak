
class Job:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Resume:
    def __init__(self, name, email, jobs):
        self.name = name
        self.email = email
        self.jobs = jobs
#func
def calculate_experience(resume):
    experience = 0
    for job in resume:
        experience += job.duration
    return experience
#no func
def print_resume(resume):
    print("Name:", resume.name)
    print("Email:", resume.email)
    print("Experience:", calculate_experience(resume.jobs))
    for job in resume.jobs:
        print(job.title, job.duration)

jobs = [Job("Developer", 2), Job("Manager", 3)]
resume = Resume("John Doe", "john.doe@example.com", jobs)

print_resume(resume)