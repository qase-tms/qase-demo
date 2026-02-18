# Queries (QQL, Qase Query Language)

***⚠️ Queries are available with [Business](https://help.qase.io/en/articles/5563727-business-plan) and [Enterprise](https://help.qase.io/en/articles/6640055-enterprise-plan) subscriptions.***

**Queries help you make analytical requests to get specific data from your Qase projects.**

Queries are based on Qase Query Language (QQL). You can access Queries from the top-left menu.

[![](https://downloads.intercomcdn.com/i/o/860792690/8fe91ed1234c171d10d962c6/tab-queries.png?expires=1771427700&signature=8e01f8f6233b4c50ac93bafda1430dda8d1346a4920f0dd897f98ba14e629ae9&req=fCYnEcB8m4hfFb4f3HP0gCYu6b31BkqEj%2FFiQKa2katSJCIqq2hOrq6oRfHH%0AbqPtixHPOdP36tLJtg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/860792690/8fe91ed1234c171d10d962c6/tab-queries.png?expires=1771427700&signature=8e01f8f6233b4c50ac93bafda1430dda8d1346a4920f0dd897f98ba14e629ae9&req=fCYnEcB8m4hfFb4f3HP0gCYu6b31BkqEj%2FFiQKa2katSJCIqq2hOrq6oRfHH%0AbqPtixHPOdP36tLJtg%3D%3D%0A)

From this page, you can manage [saved queries](https://help.qase.io/en/articles/6417205-saved-queries) and create new ones.

**[Saved Queries](https://help.qase.io/en/articles/6417205-saved-queries) can be used with the [QQL widget](https://help.qase.io/en/articles/5563698-dashboards#h_9644c6d14d).**

QQL widget allows you to leverage advanced query searches, and pin frequently used or preferred QQL searches to your *[dashboards](https://help.qase.io/en/articles/5563698-dashboards)* to facilitate quicker and more comprehensive monitoring of testing activities.

#

# Create a new query

---

You can click on either one of the two buttons to create a new query.

[![](https://downloads.intercomcdn.com/i/o/860887546/10289d9eb250694495939e98/query-create.png?expires=1771427700&signature=650c31818d2ef45f0463ac700f5513d23c76553a681fad0ea38e9a88c0440f23&req=fCYnHsF5mIVZFb4f3HP0gCb8N4kegMmlOv0lAB5KAHhPJGOXXz1ifwExX13c%0ArIxRNN20j6wcFU9llg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/860887546/10289d9eb250694495939e98/query-create.png?expires=1771427700&signature=650c31818d2ef45f0463ac700f5513d23c76553a681fad0ea38e9a88c0440f23&req=fCYnHsF5mIVZFb4f3HP0gCb8N4kegMmlOv0lAB5KAHhPJGOXXz1ifwExX13c%0ArIxRNN20j6wcFU9llg%3D%3D%0A)

Here, you can -  
1. Select the entity from the drop down

2. Write your query

3. Search the query

4. Save the query, either as a private query, or a public one.

5. Choose the fields to be displayed in the table.

[![](https://downloads.intercomcdn.com/i/o/1166967592/c0a571fe1e1ffcafa6bbf009/image.png?expires=1771427700&signature=ce3d8293366f646be913a0106f8b1519aad665f1cc7b41fbb6a695534d3ee8b8&req=dSEhEMB4moRWW%2FMW1HO4zUn%2FKHg%2FCo4%2FLsXlkr9GJJKvYrow6Ikm4oVXhkFe%0AJRRJS8wBQd7ONy2Xb7E%3D%0A)](https://downloads.intercomcdn.com/i/o/1166967592/c0a571fe1e1ffcafa6bbf009/image.png?expires=1771427700&signature=ce3d8293366f646be913a0106f8b1519aad665f1cc7b41fbb6a695534d3ee8b8&req=dSEhEMB4moRWW%2FMW1HO4zUn%2FKHg%2FCo4%2FLsXlkr9GJJKvYrow6Ikm4oVXhkFe%0AJRRJS8wBQd7ONy2Xb7E%3D%0A)

[Read more](https://help.qase.io/en/articles/6417205-saved-queries) about Public vs Private queries.

# QQL Structure

---

QQL consists of two parts: "Entity" + "Query". Both are required to perform a search.

Here are a few example:

```
entity = "defect" and status = "open"
```

```
entity = "case" and project = "DEMO" and title !~ "auth" order by id desc
```

```
entity = "result" and status = "failed" and timeSpent > 5000 and   
milestone ~ "Sprint 12"
```

```
entity = "case" and isFlaky = false and automation = "To be automated"
```

**Entity** can be selected from the drop-down, and **Projects,** by default, include all projects available to a user.

If your expression contains a syntax error, the erroneous element will be highlighted in red, as well as you will see a red "x" icon appearing in the expression field:

[![](https://downloads.intercomcdn.com/i/o/910657357/22bf2e965e6b6f617e8a459b/image.png?expires=1771427700&signature=6137aac8aeb869a9d569ccbba259357ce4692bcfb8daf0360a5b1a361cebb180&req=fSEnEMx5noRYFb4f3HP0gIcMKVtV9jWI11voxoCwj5HNmeLjbBHrtDNyaNtW%0AR0kb9nUofGe%2FYJ%2F%2B2g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/910657357/22bf2e965e6b6f617e8a459b/image.png?expires=1771427700&signature=6137aac8aeb869a9d569ccbba259357ce4692bcfb8daf0360a5b1a361cebb180&req=fSEnEMx5noRYFb4f3HP0gIcMKVtV9jWI11voxoCwj5HNmeLjbBHrtDNyaNtW%0AR0kb9nUofGe%2FYJ%2F%2B2g%3D%3D%0A)

## **Entities**

Below are the available entities. Click on an entity to skip to the attributes available for it.

* [Test case](#h_cb4adef46a)
* [Test run](#h_340289e352)
* [Test run result](#h_442329b3b5)
* [Test Plan](#h_e9113559bb)
* [Defect](#h_d6d0c91118)
* [Requirement](#h_c47f8c5b2f)

## **Expressions**

Currently, QQL supports seven expression types. They are listed here in the decreasing priority order:

|  |  |
| --- | --- |
| **Expression Type** | **Example** |
| Parenthesis | ``` ( expression ) ``` |
| Negation | ``` not expression ``` |
| Logical Expression | ``` true ```  or  ``` false ``` |
| Logical AND | ``` expression and expression ``` |
| Logical OR | ``` expression or expression ``` |
| Checking the attribute value | ``` attribute operand value ``` |
| Sorting by field | ``` ORDER BY field ASC/DESC ``` |

## **Supported operands:**

|  |  |  |
| --- | --- | --- |
| **Operand** | **Meaning** | **Works with** |
| < | less than | integer |
| <= | less than or equal to | integer |
| > | greater than | integer |
| >= | greater than or equal to | integer |
| =, is | equal to | integer, bool |
| != | not equal to | integer, bool |
| ~ | includes | string, text |
| !~ | does not include | string, text |
| in | includes (array) | array |
| not in | does not include (array) | array |
| is empty | no value |  |
| is not empty | value exists |  |

## **Data types:**

|  |  |  |
| --- | --- | --- |
| **Data type** | **Possible values** | **Supported operands** |
| Integer | 110 | >, >=, <, <=, =, != |
| String | "Example text" | ~, !~ |
| Boolean | True or False | is |
| Array | ['value 1', 'value 2']  ;  ('value 1', 'value 2')  ;  [ ] | in |
| Null | null | - |

## **Functions:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Return type** | **Arguments** | **Description** |
| currentUser() | integer | - | Returns an ID of current user |
| activeUsers() | integer | - | Returns IDs of all active users. |
| inactiveUsers() | integer | - | Returns IDs of all inactive users. |
| group() | integer | `'group name`' - input group name  `[group('name1'), group('name2')]` - an array of groups. ​ | Returns IDs of all group members. |
| now() | integer | `"+Nd" / "-Nd"`- modifies returned value, adding/subtracting N days.    In `"+Nd"`, replace **d** with  ​ **w** for weeks;  ​ **m** for months.  ​  `N must be an integer` | Returns current timestamp |
| startOfDay() | integer | '**YYYY-mm-dd**' - modifies returned value to the start of this input date.    `"+/-N[d/w/m]"` - modifies returned value by **N** days/weeks/months. | Returns timestamp of start of current day. |
| startOfWeek() | integer | '**YYYY-mm-dd**' - modifies returned value to the start of first day of the week (relative to the input date)    `"+/-N[d/w/m]"` - modifies returned value by **N** days/weeks/months. | Returns timestamp of start of current week. |
| startOfMonth() | integer | '**YYYY-mm-dd**' - modifies returned value to the start of first day of the month (relative to the input date)    `"+/-N[d/w/m]"` - modifies returned value by **N** days/weeks/months. | Returns timestamp of start of current Month. |
| endOfDay() | integer | '**YYYY-mm-dd**' - modifies returned value to the end of the input date.    `"+/-N[d/w/m]"` - modifies returned value by **N** days/weeks/months. | Returns timestamp of end of current day. |
| endOfWeek() | integer | '**YYYY-mm-dd**' - modifies returned value to the end of first day of the week (relative to the input date)    `"+/-N[d/w/m]"` - modifies returned value by **N** days/weeks/months. | Returns timestamp of end of current Week. |
| endOfMonth() | integer | '**YYYY-mm-dd**' - modifies returned value to the end of first day of the month (relative to the input date)    `"+/-N[d/w/m]"` - modifies returned value by **N** days/weeks/months. | Returns timestamp of end of current Month. |

# Entity fields

---

## Test case:

|  |  |  |
| --- | --- | --- |
| **Attribute** | **Description** | **Examples** |
| ``` id ``` | identifier | ``` id = 17 ```  ``` id != 20 ```  ``` id is 17 ```  ``` id in [1, 2, 10] ```  ``` not id in [1, 2, 10] ``` |
| ``` title ```  ``` preconditions ```  ``` postconditions ```  ``` description ``` | Test case title,    Pre/postconditions,          Description | ``` title is "first test" ```  ``` title = "first test" ```  ``` title ~ "rst" ```  ``` title in ["first test", "second test"] ``` |
| ``` author ``` | creator the test case. | ``` author in ["user1", "user2"] ```  ``` author = "user1" [or]  author = "user2" ```  ``` author = group('name') [or]  author in [group('name1'), group('name2')] ```  ``` author = activeUsers() [or]  author = inactiveUsers() ``` |
| ``` author ``` | If a test case is created by a reporter app | ``` author = [name]-reporter ```  Replace [name] with reporter name.    ``` Eg: author = pytest-reporter ```  **Reporters:**  ---  Playwright;  cucumberjs;  cypress;  jest;  newman;  testcafe;  cucumber3; cucumber4; cucumber5;  junit4; jnuit5;  testng;  pytest;  robotframework;  xctest;  phpunit;  codeception. |
| ``` cf ``` | Custom fields:  a complex attribute with a specific syntax, see examples. | ``` cf["Epic"] = "Auth" ```  ``` cf["Story"] in ["Story 1", "Story 2"] ```  ``` cf["Epic"] is null ```  ``` cf["Story"] = ["Auth", "Login"] ``` |
| ``` cfv ``` | Custom field values. (by all custom fields) | ``` cfv = "Auth" ```  ``` cfv in ["Story 1", "Story 2"] ``` |
| ``` status ```  ``` type ```  ``` behavior ```  ``` automation ```  ``` layer ```  ``` priority ```  ``` severity ``` |  | ``` status is "Actual" ```  ``` status = "Actual" ```  ``` status != "Deprecated" ```  ``` status in ["Draft", "Actual"] ``` |
| ``` created ``` | Time of case creation | ``` created >= now("-14d") ```  ``` created < startOfDay('YYYY-mm-dd') ```  ``` created < 1569430502709 ``` |
| ``` createdBy ``` | The user who created the case | ``` createdBy in ["user1", "user2"] ```  ``` createdBy = "user1" or createdBy = "user2" ``` |
| ``` updated ``` | Last modified date | ``` updated >= now("-7d") ```  ``` updated >= startOfDay('YYYY-mm-dd') ```  ``` updated < 1569430502709 ``` |
| ``` updatedBy ``` | Last modified by user | ``` updatedBy = currentUser() ```  ``` updatedBy = group('group name') ```  ``` updatedBy = 'User A' ``` |
| ``` isDeleted ``` | Check whether the case has been deleted or not | ``` isDeleted is false ```  ``` isDeleted = true ``` |
| ``` isFlaky ``` | Check whether the case has been flagged as flaky | ``` isFlaky is false ```  ``` isFlaky = true ``` |
| ``` project ``` | By default, search is performed across all projects.  If required, you can specify a project code. | ``` project = 'DEMO' ```  ``` project in ['DEMO', 'QTC'] ```  ``` project not in ['DEMO'] ``` |
| ``` suite ``` | Test case's suite title | ``` suite ~ 'auth' ```  ``` suite != 'auth' ```  ``` suiteTree = 'parent suite name' ``` |
| ``` milestone ``` | Test case's milestone title | ``` milestone = 'Sprint 24' ``` |
| ``` tags ``` | Test case's tags | ``` tags not in ['tag','tag2'] ``` |
| ``` isAiGenerated ``` | is the test generated using AIDEN? | ``` isAiGenerated = true ``` |

## Defects:

|  |  |  |
| --- | --- | --- |
| **Attribute** | **Description** | **Examples** |
| ``` id ``` | identifier | ``` id = 17 ```  ``` id != 20 ```  ``` id is 17 ```  ``` id in [1, 2, 10] ```  ``` not id in [1, 2, 10] ``` |
| ``` title ``` | Defect title | ``` title is "first test" ```  ``` title = "first test" ```  ``` title ~ "rst" ```  ``` title in ["first test", "second test"] ``` |
| ``` actual_result ``` | Actual result | ``` actual_result is "first" ```  ``` actual_result = "first" ```  ``` actual_result ~ "rst" ```  ``` actual_result in ["first", "second"] ``` |
| ``` project ``` | Project | ``` project = 'DEMO' ```  ``` project in ['DEMO', 'QTC'] ```  ``` project not in ['DEMO'] ``` |
| ``` status ``` | Statuses  ---  open; resolved; in progress; invalid | ``` status is "Open" ```  ``` status = "Resolved" ```  ``` status != "Invalid" ```  ``` status in ["Open", "Invalid"] ``` |
| ``` severity ``` | Severity  ---  undefined;  blocker;  critical;  major;  normal;  minor;  trivial | ``` severity is "blocker" ```  ``` severity = "blocker" ```  ``` severity != "blocker" ```  ``` severity in ["blocker", "critical"] ``` |
| ``` author ``` | The user who created the defect | ``` author in ["user1", "user2"] ```  ``` author = "user1" ```  ``` author = group('name') [or] author in [group('name1'), group('name2')] ```  ``` author = activeUsers() [or] author = inactiveUsers() ``` |
| ``` author ``` | If a defect has been created by a reporter app | ``` author = [name]-reporter ```  Replace [name] with reporter name.    ``` Eg: author = pytest-reporter ```  **Reporters:**  ---  Playwright;  cucumberjs;  cypress;  jest;  newman;  testcafe;  cucumber3; cucumber4; cucumber5;  junit4; jnuit5;  testng;  pytest;  robotframework;  xctest;  phpunit;  codeception. |
| ``` createdBy ``` | The user who created the defect | ``` createdBy in ["user1", "user2"] ```  ``` createdBy = "user1" or createdBy = "user2" ``` |
| ``` created ``` | Time of creation | ``` created >= now("-14d") ```  ``` created >= startOfDay('YYYY-mm-dd') ```  ``` created < 1569430502709 ``` |
| ``` updated ``` | Time of update | ``` updated >= now("-14d") ```  ``` updated >= startOfDay('YYYY-mm-dd') ```  ``` updated < 1569430502709 ``` |
| ``` resolved ``` | Time of resolution | ``` resolved >= now("-14d") ```  ``` resolved > startOfDay('YYYY-mm-dd') ```  ``` resolved < 1569430502709 ``` |
| ``` isDeleted ``` | Whether the defect is deleted | ``` isDeleted is false ```  ``` isDeleted = true ``` |
| ``` isResolved ``` | Whether the defect is resolved | ``` isResolved is false ```  ``` isResolved = true ``` |
| ``` milestone ``` | Defect's milestone title | ``` milestone = 'Milestone title' ``` |
| ``` cfv ``` | Custom field values (by all custom fields) | ``` cfv = "Auth" ```  ``` cfv in ["Story 1", "Story 2"] ```  ``` cfv is empty ``` |
| ``` cf ``` | Custom fields:  a complex attribute with a specific syntax, see examples. | ``` cf["Epic"] = "Auth" ```  ``` cf["Story"] in ["Story 1", "Story 2"] ```  ``` cf["Epic"] is null ```  ``` cf["Story"] = ["Auth", "Login"] ``` |
| ``` tags ``` | Defect's tags | ``` tags not in ['tag'] ``` |

## Test Run:

|  |  |  |
| --- | --- | --- |
| **Attribute** | **Description** | **Examples** |
| ``` id ``` | Identifier | ``` id = 17 ```  ``` id != 20 ```  ``` id is 17 ```  ``` id in [1, 2, 10] ```  ``` id not in [1, 2, 10] ``` |
| ``` title ``` | Title | ``` title is "first test" ```  ``` title = "first test" ```  ``` title ~ "rst" ```  ``` title in ["first test", "second test"] ``` |
| ``` description ``` | Description | ``` description is "first" ```  ``` description = "first" ```  ``` description ~ "rst" ```  ``` description in ["first", "second"] ``` |
| ``` project ``` | Project | ``` project = 'DEMO' ```  ``` project in ['DEMO', 'QTC'] ```  ``` project not in ['DEMO'] ``` |
| ``` plan ``` | Title of the plan used | ``` plan = 'Regression' ``` |
| ``` status ``` | Status | ``` status is "passed" ```  ``` status = "in progress" ```  ``` status != "aborted" ```  ``` status in ["failed", "aborted"] ``` |
| ``` author ``` | The user who created the run | ``` author in ["user1", "user2"] ```  ``` author = "user1" or createdBy = "user2" ```  ``` author = group('name') [or]  author in [group('name1'), group('name2')] ```  ``` author = activeUsers() [or] author = inactiveUsers() ``` |
| ``` author ``` | If a test run has been created by a reporter app | ``` author = [name]-reporter ```  Replace [name] with reporter name.    ``` Eg: author = pytest-reporter ```  **Reporters:**  ---  Playwright;  cucumberjs;  cypress;  jest;  newman;  testcafe;  cucumber3; cucumber4; cucumber5;  junit4; jnuit5;  testng;  pytest;  robotframework;  xctest;  phpunit;  codeception. |
| ``` createdBy ``` | The user who created the run | ``` createdBy in ["user1", "user2"] ```  ``` createdBy = "user1"   or  createdBy = "user2" ``` |
| ``` started ``` | Time of start | ``` started >= now("-14d") ```  ``` started >= startOfDay('YYYY-mm-dd') ```  ``` started < 1569430502709 ``` |
| ``` ended ``` | Time of finish | ``` ended >= now("-14d") ```  ``` ended >= startOfDay('YYYY-mm-dd') ```  ``` ended < 1569430502709 ``` |
| ``` deleted ``` | Time of removal | ``` deleted >= now("-14d") ```  ``` deleted < startOfDay('YYYY-mm-dd') ```  ``` deleted < 1569430502709 ``` |
| ``` isDeleted ``` | Whether the run is deleted | ``` isDeleted is false ```  ``` isDeleted = true ``` |
| ``` isStarted ``` | Whether the run is started | ``` isStarted is false ```  ``` isStarted = true ``` |
| ``` isEnded ``` | Whether the run is ended | ``` isEnded is false ```  ``` isEnded = true ``` |
| ``` isPublic ``` | Whether the run has a public link | ``` isPublic is false ```  ``` isPublic = true ``` |
| ``` isAutotest ``` | Whether the run is automated | ``` isAutotest is false ```  ``` isAutotest = true ``` |
| ``` Milestone ``` | Run's milestone title | ``` milestone = 'Milestone title' ``` |
| ``` cfv ``` | Custom field values (by all custom fields) | ``` cfv = "Auth" ```  ``` cfv in ["Story 1", "Story 2"] ```  ``` cfv is empty ``` |
| ``` cf ``` | Custom fields:  a complex attribute with a specific syntax, see examples. | ``` cf["Epic"] = "Auth" ```  ``` cf["Story"] in ["Story 1", "Story 2"] ```  ``` cf["Epic"] is null ```  ``` cf["Story"] = ["Auth", "Login"] ``` |
| ``` tags ``` | Run's tags | ``` tags not in ['tag_name'] ``` |

## Test Run Results:

|  |  |  |
| --- | --- | --- |
| **Attribute** | **Description** | **Examples** |
| ``` id ``` | Identifier | ``` caseId = 17 ```  ``` caseId != 20 ```  ``` caseId is 17 ```  ``` caseId in [1, 2, 10] ```  ``` not caseId in [1, 2, 10] ``` |
| ``` comment ``` | Comment | ``` comment is "first test" ```  ``` comment = "first test" ```  ``` comment ~ "rst" ```  ``` comment in ["first test", "second test"] ``` |
| ``` case ``` | Test Run Result's case title | ``` case is "first" ```  ``` case = "first" ```  ``` case ~ "rst" ```  ``` case in ["first", "second"] ``` |
| ``` run ``` | Test Run title | ``` run is "first" ```  ``` run = "first" ```  ``` run ~ "rst" ```  ``` run in ["first", "second"] ``` |
| ``` project ``` | Project | ``` project = 'DEMO' ```  ``` project in ['DEMO', 'QTC'] ```  ``` project not in ['DEMO'] ``` |
| ``` status ``` | Status  ---  Passed;  Failed;  Blocked;  Retest;  Skipped;  Deleted;  In progress;  Invalid | ``` status is "Invalid" ```  ``` status = "Invalid" ```  ``` status != "Invalid" ```  ``` status in ["Invalid", "Failed"] ``` |
| ``` author ```  ``` assignee ``` | The user who created the result | ``` author in ["user1", "user2"] ```  ``` author = "user1" or createdBy = "user2" ```  ``` author = group('name') [or] author in [group('name1'), group('name2')] ```  ``` author = activeUsers() [or] author = inactiveUsers() ``` |
| ``` author ```  ``` assignee ``` | If a test run result has been created by a reporter app | ``` author = [name]-reporter ```  Replace [name] with reporter name.    ``` Eg: author = pytest-reporter ```  **Reporters:**  ---  Playwright;  cucumberjs;  cypress;  jest;  newman;  testcafe;  cucumber3; cucumber4; cucumber5;  junit4; jnuit5;  testng;  pytest;  robotframework;  xctest;  phpunit;  codeception. |
| ``` createdBy ``` | The user who created the run | ``` createdBy in ["user1", "user2"] ```  ``` createdBy = "user1" or createdBy = "user2" ``` |
| ``` ended ``` | Time of finish | ``` ended >= now("-14d") ```  ``` ended >= startOfDay('YYYY-mm-dd') ```  ``` ended < 1569430502709 ``` |
| ``` isDeleted ``` | Whether the result is deleted | ``` isDeleted is false ```  ``` isDeleted = true ``` |
| ``` timeSpent ``` | Time spent (in milliseconds) | ``` timeSpent > 10000 ``` |

## Test Plan:

|  |  |  |
| --- | --- | --- |
| **Attribute** | **Description** | **Examples** |
| ``` id ``` | Identifier | ``` id = 17 ```  ``` id != 20 ```  ``` id is 17 ```  ``` id in [1, 2, 10] ```  ``` not id in [1, 2, 10] ``` |
| ``` title ``` | Title | ``` title is "first test" ```  ``` title = "first test" ```  ``` title ~ "rst" ```  ``` title in ["first test", "second test"] ``` |
| ``` description ``` | Plan's description | ``` description is "first test" ```  ``` description = "first test" ```  ``` description ~ "rst" ```  ``` description in ["first test", "second test"] ``` |
| ``` project ``` | Project | ``` project = 'DEMO' ```  ``` project in ['DEMO', 'QTC'] ```  ``` project not in ['DEMO'] ``` |
| ``` created ``` | Time of creation | ``` created >= now("-14d") ```  ``` created >= startOfDay('YYYY-mm-dd') ```  ``` created < 1569430502709 ``` |
| ``` updated ``` | Time of the last update | ``` updated >= now("-14d") ```  ``` updated >= startOfDay('YYYY-mm-dd') ```  ``` updated < 1569430502709 ``` |
| ``` deleted ``` | Time of deletion | ``` deleted >= now("-14d") ```  ``` deleted >= startOfDay('YYYY-mm-dd') ```  ``` deleted < 1569430502709 ``` |
| ``` isDeleted ``` | Whether the plan is deleted | ``` isDeleted is false ```  ``` isDeleted = true ``` |

## Requirement:

|  |  |  |
| --- | --- | --- |
| **Attribute** | **Description** | **Examples** |
| ``` id ``` | Identifier | ``` id = 17 ```  ``` id != 20 ```  ``` id is 17 ```  ``` id in [1, 2, 10] ```  ``` not id in [1, 2, 10] ``` |
| ``` parent ``` | Parent requirement's title | ``` parent is "first test" ```  ``` parent = "first test" ```  ``` parent ~ "rst" ```  ``` parent in ["first test", "second test"] ``` |
| ``` project ``` | Project | ``` project = 'DEMO' ```  ``` project in ['DEMO', 'QTC'] ```  ``` project not in ['DEMO'] ``` |
| ``` author ``` | The user who created the requirement | ``` author in ["user1", "user2"] ```  ``` author = "user1"     or  createdBy = "user2" ```  ``` author = group('name') [or] author in [group('name1'), group('name2')] ```  ``` author = activeUsers() [or] author = inactiveUsers() ``` |
| ``` createdBy ``` | The user who created the requirement | ``` createdBy in ["user1", "user2"] ```  ``` createdBy = "user1"  or  createdBy = "user2" ``` |
| ``` title ``` | Title | ``` title is "first test" ```  ``` title = "first test" ```  ``` title ~ "rst" ```  ``` title in ["first test", "second test"] ``` |
| ``` description ``` | Description | ``` description is "first test" ```  ``` description = "first test" ```  ``` description ~ "rst" ```  ``` description in ["first test", "second test"] ``` |
| ``` status ``` | Status  ---  valid;  draft;  review;  rework;  finish;  implemented;  not-testable;  obsolete. | ``` status = 'valid' ``` |
| ``` type ``` | Type  ---  epic;  user-story;  feature. | ``` type = 'epic' ``` |
| ``` created ``` | Time of creation | ``` created >= now("-14d") ```  ``` created >= startOfDay('YYYY-mm-dd') ```  ``` created < 1569430502709 ``` |
| ``` updated ``` | Time of last update | ``` updated >= now("-14d") ```  ``` updated >= startOfDay('YYYY-mm-dd') ```  ``` updated < 1569430502709 ``` |
| ``` deleted ``` | Time of deletion | ``` deleted >= now("-14d") ```  ``` deleted >= startOfDay('YYYY-mm-dd') ```  ``` deleted < 1569430502709 ``` |
| ``` isDeleted ``` | Whether the requirement is deleted | ``` isDeleted is false ```  ``` isDeleted = true ``` |

# Examples of Queries

```
entity = "case" and isDeleted is true
```

```
entity = "case" and created >= now("-3d")
```

```
entity = "case" and created <= now("-3d")
```

```
entity = "case" and isDeleted is true and project in ["QTC"]
```

```
project = "QTC" and automation = "Not automated"
```

```
project = "MR" and automation != "Automated"
```

```
project = "QTC" and status in ["Draft", "Actual"]
```

```
entity = "defect" and status !="Open" and severity = "Not set"
```

```
entity = "defect" and status !=1 and severity = 0
```

```
entity = "defect" and status !=1 and severity = 0 and cfv in ["1", "2"]
```

```
entity = "defect" and status !="Open" and severity != "Not set" and milestone is empty
```

```
entity = "defect" and status !="Open" and severity != "Not set" and cf["Defect URL"] is not null
```

```
entity = "case" and author != "CEO" and updated <= now("-1d") and isFlaky is false
```

```
entity = "case" and author != "CEO" and updated <= now("-1d") and project in ('QASE', 'NQASE') and id = 1
```

---

# QQL **Grouping and Aggregate**

In addition to filtering and sorting, QQL also supports simple summaries that help you understand your data at a higher level.

This is useful when you want counts, grouped information, or quick overviews.

You can use:

* `SELECT()` — choose what fields or calculations to return
* `COUNT()` — count matching records
* `MIN()` / `MAX()` — find the earliest or latest value
* `FIRST()` / `LAST()` — return the first or last item in the current sort order
* `GROUP BY` — group results by a field
* `HAVING` — filter groups after they are created

### **Fields Supported in `SELECT()` and `GROUP BY`**

Many fields can be used with `SELECT`, `GROUP BY`, and aggregations.

The table below shows which fields are supported.

|  |  |  |  |
| --- | --- | --- | --- |
| Field | Supported for select() | Supported for GROUP BY and Aggregates | Entity |
| **Basic Fields** |  |  |  |
| `id` | ✅ Yes | ✅ Yes | case, defect, run, result, plan, requirement |
| `title` | ✅ Yes | ✅ Yes | case, defect, run, plan, requirement |
| `description` | ✅ Yes | ✅ Yes | case, run, plan, requirement |
| `preconditions` | ✅ Yes | ✅ Yes | case |
| `postconditions` | ✅ Yes | ✅ Yes | case |
|  |  |  |  |
| Status & Type |  |  |  |
| `status` | ✅ Yes | ✅ Yes | case, defect, run, result, requirement |
| `type` | ✅ Yes | ✅ Yes | case, requirement |
| `behavior` | ✅ Yes | ✅ Yes | case |
| `automation` | ✅ Yes | ✅ Yes | case |
| `isManual` | ✅ Yes | ✅ Yes | case |
| `isToBeAutomated` | ✅ Yes | ✅ Yes | case |
| `isMuted` | ✅ Yes | ✅ Yes | case |
|  |  |  |  |
| Priority & Severity |  |  |  |
| `severity` | ✅ Yes | ✅ Yes | case, defect |
| `priority` | ✅ Yes | ✅ Yes | case |
| `layer` | ✅ Yes | ✅ Yes | case |
| `isFlaky` | ✅ Yes | ✅ Yes | case |
|  |  |  |  |
| Relations |  |  |  |
| `project` | ✅ Yes | ✅ Yes | case, defect, run, plan, result, requirement |
| `milestone` | ✅ Yes | ✅ Yes | case, defect |
| `suite` | ✅ Yes | ✅ Yes | case |
|  |  |  |  |
| Timestamps |  |  |  |
| `created` | ✅ Yes | ✅ Yes | case, defect, plan, requirement |
| `updated` | ✅ Yes | ✅ Yes | case, defect, plan, requirement |
| `deleted` | ✅ Yes | ✅ Yes | run, plan, requirement |
|  |  |  |  |
| Author Fields |  |  |  |
| `author` | ✅ Yes | ✅ Yes | case, defect, run, result, requirement |
| `updatedBy` | ✅ Yes | ✅ Yes | case |
| `createdBy` | ✅ Yes | ✅ Yes | case, defect, run, result, requirement |
|  |  |  |  |
| Boolean Fields |  |  |  |
| `isDeleted` | ✅ Yes | ✅ Yes | case, defect, run, result, plan, requirement |
|  |  |  |  |
| Fields with CustomBuilder |  |  |  |
| `tags` | ✅ Yes (WHERE) | ❌ No | case, defect, run |
| `isAiGenerated` | ✅ Yes (WHERE) | ❌ No | case |
| `cfv` | ✅ Yes (WHERE) | ❌ No | case, defect, run |
|  |  |  |  |
| Custom Fields |  |  |  |
| `cf["field"]` | ✅ Yes (WHERE) | ❌ No | case, defect, run |

## **Advanced Query Examples**

Examples that show how to use grouping and aggregates for quick summaries.

|  |  |  |
| --- | --- | --- |
| Entity | Query | Description |
| Test case | `SELECT (COUNT(*))` | Find how many test cases exist in total |
| Test case | `SELECT (COUNT(*)) status = 'actual' and project = "DEMO" and severity = "critical" and priority = "High"` | Find how many test cases in project DEMO have: status actual, severity critical, and priority High |
| Test case | `SELECT (status, COUNT(*)) GROUP BY status` | For each status, find how many test cases have this status |
| Test case | `SELECT (status, project, severity, COUNT(*)) GROUP BY status, project, severity` | For each combination of status + project + severity, find how many test cases are in this group |
| Test case | `SELECT (MIN(created), MAX(created))` | Find the oldest and the newest creation dates of test cases |
| Test case | `SELECT (MIN(updated), MAX(updated))` | Find the earliest and latest update dates of test cases |
| Test case | `SELECT (FIRST(title), LAST(title))` | Get the first and the last test case titles in the current result order |
| Test case | `SELECT (status, COUNT(*)) GROUP BY status HAVING COUNT(*) > 0` | For each status, show how many test cases it has, but only if the number is more than 0 |
|  |  |  |
| Defect | `SELECT (COUNT(*))` | Find how many defects exist in total |
| Defect | `SELECT (COUNT(*)) status = 'open' and project = "DEMO" and severity = "critical"` | Find how many defects are open, in project DEMO, and with critical severity |
| Defect | `SELECT (status, COUNT(*)) GROUP BY status` | For each status, find how many defects have this status |
| Defect | `SELECT (status, project, severity, COUNT(*)) GROUP BY status, project, severity` | For each combination of status + project + severity, find how many defects are in this group |
| Defect | `SELECT (FIRST(title), LAST(title))` | Get the first and the last defect titles in the current result order |
| Defect | `SELECT (severity, COUNT(*)) GROUP BY severity HAVING COUNT(*) > 0` | For each severity level, show how many defects it has, but only if there is at least one defect |
|  |  |  |
| Test run | `SELECT (COUNT(*))` | Find how many **test runs** exist in total |
| Test run | `SELECT (COUNT(*)) status = 'in progress' and project = "DEMO"` | Find how many test runs are in progress in project DEMO |
| Test run | `SELECT (status, COUNT(*)) GROUP BY status` | For each status, find how many test runs have this status |
| Test run | `SELECT (FIRST(title), LAST(title))` | Get the first and the last test run titles in the current result order |
| Test run | `SELECT (status, COUNT(*)) GROUP BY status HAVING COUNT(*) > 0` | For each status, show how many test runs it has, but only if there is at least one run |
|  |  |  |
| Run result | `SELECT (COUNT(*))` | Find how many test results exist in total |
| Run result | `SELECT (COUNT(*)) status = 'active' and run = "test"` | Find how many test results have status active in the run named "test" |
| Run result | `SELECT (status, COUNT(*)) GROUP BY status` | For each status, find how many test results have this status |
| Run result | `SELECT (status, COUNT(*)) GROUP BY status HAVING COUNT(*) > 0` | For each status, show how many test results it has, but only if there is at least one result |
| Plan | `SELECT (COUNT(*))` | Find how many test plans exist in total |
| Plan | `SELECT (COUNT(*)) project = "DEMO"` | Find how many test plans belong to project DEMO |
| Plan | `SELECT (project, COUNT(*)) GROUP BY project` | For each project, find how many test plans this project has |
| Plan | `SELECT (MIN(created), MAX(created))` | Find the oldest and the newest creation dates of all test plans |
| Plan | `SELECT (MIN(updated), MAX(updated))` | Find the earliest and the latest update dates of all test plans |
| Plan | `SELECT (FIRST(title), LAST(title))` | Get the first and the last test plan titles in the current result order |
| Plan | `SELECT (project, COUNT(*)) GROUP BY project HAVING COUNT(*) > 0` | For each project, show how many test plans it has, but only if the number is greater than 0 |
|  |  |  |
| Requirement | `SELECT (COUNT(*))` | Find how many requirements exist in total |
| Requirement | `SELECT (COUNT(*)) status = 'valid' and project = "DEMO" and type = 'user-story'` | Find how many requirements in project DEMO have status valid and type user-story |
| Requirement | `SELECT (status, COUNT(*)) GROUP BY status` | For each status, find how many requirements have this status |
| Requirement | `SELECT (status, project, type, COUNT(*)) GROUP BY status, project, type` | For each combination of status + project + type, find how many requirements are in this group |
| Requirement | `SELECT (MIN(created), MAX(created))` | Find the oldest and the newest creation dates of all requirements |
| Requirement | `SELECT (MIN(updated), MAX(updated))` | Find the earliest and the latest update dates of all requirements |
| Requirement | `SELECT (FIRST(title), LAST(title))` | Get the first and the last requirement titles in the current result order |
| Requirement | `SELECT (status, COUNT(*)) GROUP BY status HAVING COUNT(*) > 0` | For each status, show how many requirements it has, but only if there is at least one requirement with this status |

# Export Query results

Query results can be exported as a CSV file. The exported CSV will include only the columns currently selected in your view.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1817114607/8e0f05c5d20767f607beed1f6157/image.png?expires=1771427700&signature=3a7903b55ba2b71ea483ca02b02e351b6c37edec7099e8640ef796a7a5a5ffb8&req=dSgmEch%2FmYdfXvMW1HO4zTEMEgDYklBUlFPCngEI4K%2FF7s7te9%2BixNb49Cfz%0A9nYs0gIC31SGJlIKo%2Fk%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1817114607/8e0f05c5d20767f607beed1f6157/image.png?expires=1771427700&signature=3a7903b55ba2b71ea483ca02b02e351b6c37edec7099e8640ef796a7a5a5ffb8&req=dSgmEch%2FmYdfXvMW1HO4zTEMEgDYklBUlFPCngEI4K%2FF7s7te9%2BixNb49Cfz%0A9nYs0gIC31SGJlIKo%2Fk%3D%0A)

You are free to leave the Queries screen while the export is prepared. You'll see a notification when the export is ready for download.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1831113161/4972570285945f1660600779c1b1/image.png?expires=1771427700&signature=f2d9fd0aac606aeb5f7d4c74d59fca010503e3075d136da4d7eebdc63f6819b1&req=dSgkF8h%2FnoBZWPMW1HO4zVYHhtZ1y6UGGAXPYvfgO2EOvYEXD38blRUk4klG%0At8FqS6hkfqtPXCiWvR4%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1831113161/4972570285945f1660600779c1b1/image.png?expires=1771427700&signature=f2d9fd0aac606aeb5f7d4c74d59fca010503e3075d136da4d7eebdc63f6819b1&req=dSgkF8h%2FnoBZWPMW1HO4zVYHhtZ1y6UGGAXPYvfgO2EOvYEXD38blRUk4klG%0At8FqS6hkfqtPXCiWvR4%3D%0A)

---

Related Articles

[Getting Started](https://help.qase.io/en/articles/5563688-getting-started)[Defects](https://help.qase.io/en/articles/5563710-defects)[Jira Cloud](https://help.qase.io/en/articles/6417207-jira-cloud)[Asana](https://help.qase.io/en/articles/6417211-asana)[Jira Server/Datacenter Plugin installation](https://help.qase.io/en/articles/6417212-jira-server-datacenter-plugin-installation)