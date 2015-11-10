import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

### For each of these three tables, find the number of rows in the table and
### the number of unique students in the table. To find the number of unique
### students, you might want to create a set of the account keys in each table.

def findRowsAndUniqueStudents(collection, unique_key):
  rows = 0
  students = set()

  for row in collection:
    rows += 1
    students.add(row[unique_key])

  return rows, len(students)

enrollment_num_rows, enrollment_num_unique_students = findRowsAndUniqueStudents(
  enrollments, "account_key")

engagement_num_rows, engagement_num_unique_students = findRowsAndUniqueStudents(
  daily_engagement, "acct")

submission_num_rows, submission_num_unique_students = findRowsAndUniqueStudents(
  project_submissions, "account_key")

print "enrollment %d %d" % (enrollment_num_rows, enrollment_num_unique_students)
print "engagement %d %d" % (engagement_num_rows, engagement_num_unique_students)
print "submission %d %d" % (submission_num_rows, submission_num_unique_students)
