import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

def renameKeyInListOfDict(collection, source_key, dest_key):
  for item in collection:
    item[dest_key] = item[source_key]
    del item[source_key]

renameKeyInListOfDict(daily_engagement, "acct", "account_key")

def findRowsAndUniqueStudents(collection, unique_key="account_key"):
  rows = 0
  students = set()

  for row in collection:
    rows += 1
    students.add(row[unique_key])

  return rows, students

enrollment_num_rows, enrollment_unique_students = findRowsAndUniqueStudents(
  enrollments)
enrollment_num_unique_students = len(enrollment_unique_students)

engagement_num_rows, engagement_unique_students = findRowsAndUniqueStudents(
  daily_engagement)
engagement_num_unique_students = len(engagement_unique_students)

submission_num_rows, submission_unique_students = findRowsAndUniqueStudents(
  project_submissions)
submission_num_unique_students = len(submission_unique_students)

print "enrollment %d %d" % (enrollment_num_rows, enrollment_num_unique_students)
print "engagement %d %d" % (engagement_num_rows, engagement_num_unique_students)
print "submission %d %d" % (submission_num_rows, submission_num_unique_students)
