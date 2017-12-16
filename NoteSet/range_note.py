# -*- coding= utf-8 -*-

job_info = dict(
    sex=None, location=0, age_max=0, education=2, work_experience_min=0, work_experience_max=0,
    job_name=None, company_preference=[], manage_experience=True,
    salary_min=0, salary_max=0, welfare=[], skill=[], school_preference=[], key_word=[]
)
for level in range(5)[job_info['education']:]:
    print(level)
