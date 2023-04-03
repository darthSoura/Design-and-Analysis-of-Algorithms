def schedule_jobs(weights, lengths):
    
    n =len(weights)
    
    jobs_score = [(i, weights[i]/lengths[i]) for i in range(n)]    
    jobs_score_sorted = sorted(jobs_score, key=lambda x: x[1], reverse=True)
    schedule = [job[0] for job in jobs_score_sorted]
    return schedule

weights = [2,1,3,4]
lengths = [3,4,2,1]

schedule = schedule_jobs(weights, lengths)
schedule = [i + 1 for i in schedule]
print(schedule)
