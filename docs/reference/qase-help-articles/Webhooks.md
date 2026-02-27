# Webhooks

***⚠️Webhooks are available in [Startup](https://help.qase.io/en/articles/5563728-startup-plan), [Business](https://help.qase.io/en/articles/5563727-business-plan), and [Enterprise](https://help.qase.io/en/articles/6640055-enterprise-plan) subscriptions***

Webhooks in Qase allow you to create a connection between your own resources and Qase so that when a specific event takes place in Qase, it also sends a request to an endpoint you defined for that particular event.

Setting up a webhook is easy - navigate to the *Settings* of a project where webhooks will be needed, then select *Webhooks* and hit "Create new webhook":

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1208547245/61981ee5dc3d507bc1b3a73fa3cf/72729.png?expires=1771427700&signature=0e1565948398d5bda05f393aa000b47cfc87c8c83403f0849026743d60dc5cf5&req=dSInHsx6moNbXPMW1HO4zc640m%2FVOFUPH0D1U0PI6UhYaFg2tsItQSHn8fDh%0APozYmqvEy%2BtOCFEzSC0%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1208547245/61981ee5dc3d507bc1b3a73fa3cf/72729.png?expires=1771427700&signature=0e1565948398d5bda05f393aa000b47cfc87c8c83403f0849026743d60dc5cf5&req=dSInHsx6moNbXPMW1HO4zc640m%2FVOFUPH0D1U0PI6UhYaFg2tsItQSHn8fDh%0APozYmqvEy%2BtOCFEzSC0%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1208550745/202af23854809c231fefdcd3f9e5/webhooks.gif?expires=1771427700&signature=42875f0555d674cc8dc3776036a51db167003372b4fe07100c0a9d813132184b&req=dSInHsx7nYZbXPMW1HO4zYV6Tp%2BQwbX5D%2FJ7%2FmhgOixqvUEvggQkPVqfuVew%0ABTNO%2FlHRXOM7KU3UN0E%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1208550745/202af23854809c231fefdcd3f9e5/webhooks.gif?expires=1771427700&signature=42875f0555d674cc8dc3776036a51db167003372b4fe07100c0a9d813132184b&req=dSInHsx7nYZbXPMW1HO4zYV6Tp%2BQwbX5D%2FJ7%2FmhgOixqvUEvggQkPVqfuVew%0ABTNO%2FlHRXOM7KU3UN0E%3D%0A)

Webhooks can be enabled and disabled as needed:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1208549447/9287054389c017d6b9fd8efe3fd9/74920.png?expires=1771427700&signature=09dc24a2790a0f755eacc76ae5e1986e4986b66639aaa8c7f5d05b519b9a01f1&req=dSInHsx6lIVbXvMW1HO4za2ecs2swPw52I30kjguDh2a9f9WdRCEYgx5%2FOSF%0AK%2FRRsgoTBwDfsINAdxQ%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1208549447/9287054389c017d6b9fd8efe3fd9/74920.png?expires=1771427700&signature=09dc24a2790a0f755eacc76ae5e1986e4986b66639aaa8c7f5d05b519b9a01f1&req=dSInHsx6lIVbXvMW1HO4za2ecs2swPw52I30kjguDh2a9f9WdRCEYgx5%2FOSF%0AK%2FRRsgoTBwDfsINAdxQ%3D%0A)

A webhook will be automatically disabled based on the following conditions:

* the endpoint where webhook is sent does not return any response within 15 seconds of the payload being sent
* within 2 days period of time, the webhook was not able ​to send a successful request to the specified endpoint

When a webhook is disabled due to failed attempts above, you will receive an email notification about it.

There are a few parameters you need to define for a new webhook:

* *Basic:*

  + *Title:* a name for your webhook.
  + *Endpoint:* a URL address that is configured on your side and is accessible to the public web; this address will be where Qase sends a request upon a defined event happening.
  + *Secret:* we are sending this text as an X-Qase-Secret header so that you can authenticate your webhook.
* *Events:* in this section, you will set up a trigger for Qase to send a request to the endpoint; there are several to choose from, and it is also possible to enable multiple event-triggers for a single endpoint.

  + *[Test Cases](https://docs.qase.io/general/webhooks/test-case):*

    - Create test case
    - Update test case
    - Delete test case
    - Clone test case
  + *[Test Suites](https://docs.qase.io/general/webhooks/test-suite):*

    - Create test suite
    - Update test suite
    - Delete test suite
    - Clone test suite
  + *[Test Plans](https://docs.qase.io/general/webhooks/test-plan):*

    - Create test plan
    - Update test plan
    - Delete test plan
  + *[Shared Steps](https://docs.qase.io/general/webhooks/shared-step):*

    - Create shared step
    - Update shared step
    - Delete shared step
  + *[Milestones](https://docs.qase.io/general/webhooks/milestone):*

    - Create milestone
    - Update milestone
    - Delete milestone
  + *[Custom Fields](https://docs.qase.io/general/webhooks/custom-field):*

    - Create custom field
    - Update custom field
    - Delete custom field
  + *[Test Runs](https://docs.qase.io/general/webhooks/test-run):*

    - Test run start
    - Test run aborted
    - Test cases added to run
    - Delete test run
    - Complete test run
    - Public link turned on
  + *[Defects](https://docs.qase.io/general/webhooks/defect):*

    - Create defect
    - Resolve defect
    - Delete defect
  + *[Reviews](https://docs.qase.io/general/webhooks/test-review)*:

    - Create test review
    - Update test review
    - Approval status change
    - Reviewer added
    - Reviewer removed
    - Merge test review
    - Reopen test review
    - Comment test review
    - Decline test review
    - Delete test review
  + *Results:*

    - Create test run results
    - Update test run results
    - Delete test run results

---

Related Articles

[Milestones](https://help.qase.io/en/articles/5563715-milestones)[GitHub](https://help.qase.io/en/articles/6417206-github)[Jira Cloud](https://help.qase.io/en/articles/6417207-jira-cloud)[GitHub](https://help.qase.io/en/articles/7210938-github)[How do I find my project code?](https://help.qase.io/en/articles/9787250-how-do-i-find-my-project-code)