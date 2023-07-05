from jira import JIRA

jiraOptions = {'server': "https://fleetstudio.atlassian.net"}
  
jira = JIRA(options=jiraOptions, basic_auth=(
    "tmanthiriyappan@fleetstudio.com", "ATATT3xFfGF0CnooPsHBgfbCTTKvgiobqxY2tqeMnyDiaE8L6GPmbF2T_nCAe-hrkcUXrp4VdVgRzCA1XICKfHfa-aunECVepkQJ-pYc836_CJGDRy_MZwGMbdY-Z2jJoUgU1ZnbF7Je1k8SB0KKs_c4ULfEQ_370TgHxu_UW-9GraLDtnAS2Yc=A7DB126E"))
  

for singleIssue in jira.search_issues(jql_str='project = Wally'):
    print('single issue', singleIssue.fields.comment.comments)
    # print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary,
    #                          singleIssue.fields.reporter.displayName))