# Test Cases

## Overview

A Test Case in Qase is a specific set of instructions and conditions that outline a test to be carried out successfully. It includes testing procedures, necessary inputs, execution conditions, and expected results to achieve a testing objective

In Qase, you can define various parameters and expected outcomes of a particular testing scenario.

## Create a test case

---

### a) create a Quick case

Quickly create a test case by clicking the "**+ Create quick test**" row in a Suite and type out a title. Add other details later if needed.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554811243/a206ff2ea92fb9edc2d792464a59/quick+create.gif?expires=1771427700&signature=50b94dd9e90c3c96966313a70d74158c9c7e9cc4222cf3e1ee51b218d8ad9647&req=dSUiEsF%2FnINbWvMW1HO4zR9B%2BtjQd6k2CvG9WCPXkwNCvvNQVrtLSjX6N%2F8z%0AaB9FmJRiS0njzoTYqDA%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554811243/a206ff2ea92fb9edc2d792464a59/quick+create.gif?expires=1771427700&signature=50b94dd9e90c3c96966313a70d74158c9c7e9cc4222cf3e1ee51b218d8ad9647&req=dSUiEsF%2FnINbWvMW1HO4zR9B%2BtjQd6k2CvG9WCPXkwNCvvNQVrtLSjX6N%2F8z%0AaB9FmJRiS0njzoTYqDA%3D%0A)

### b) create a Detailed case

The second method lets you fully detail your new Test Case. Click the "**+ Case**" button above the Suite structure in the repository to begin. You'll be guided in setting up your new Test Case and providing all the necessary information.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554811335/8b8fb495ecc00fa519852abb4692/create+manually.gif?expires=1771427700&signature=ed4ce7c73497b64e2f205bb8d16a9e557022698f9d4d5243474255a396fd10c2&req=dSUiEsF%2FnIJcXPMW1HO4zS%2FSZ6HMyR%2FelEQW6Q7AuYqUNul2DCbDTZwKc3vI%0ArgqUE8q%2F63GmAZlCKH8%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554811335/8b8fb495ecc00fa519852abb4692/create+manually.gif?expires=1771427700&signature=ed4ce7c73497b64e2f205bb8d16a9e557022698f9d4d5243474255a396fd10c2&req=dSUiEsF%2FnIJcXPMW1HO4zS%2FSZ6HMyR%2FelEQW6Q7AuYqUNul2DCbDTZwKc3vI%0ArgqUE8q%2F63GmAZlCKH8%3D%0A)

## Test Case Properties

---

Test Case properties can be divided into several sections:

* [Basic Fields](https://help.qase.io/en/articles/6705423-workspace-management-fields)
* Conditions
* [Tags](https://help.qase.io/en/articles/5563696-tags)
* [Attachments](https://help.qase.io/en/articles/5563708-attachments)
* [Parameters](https://help.qase.io/en/articles/6640037-test-case-parameters)
* Test Case Steps

### Basic fields

You will define the following Test Case properties:

1. *Title:* define the name of a test case
2. *Status:* can be either Active, Draft, or Deprecated
3. *Description:* additional details for more context about a test case
4. *Suite:* choose here which Test Suite your new case belongs to
5. *Severity:* can be either Trivial, Minor, Normal, Major, Critical, Blocker, or Not Set
6. *Priority:* can be either Low, Medium, High, or Not Set
7. *Type:* select what type of testing is applicable for your test case
8. *Layer:* pick a layer of the test case, whether it's an end-to-end, API, or a unit test
9. *Is flaky:* if a test case is unstable, you can mark it as flaky
10. *[Milestone:](https://help.qase.io/en/articles/5563715-milestones)* select whether a test case is related to one of your Milestones, which you can create separately
11. *Behavior:* can be either Destructive, Negative, Positive, or Not Set
12. *Automation Status:* you can choose from Manual or Automated
13. *To be automated*: a checkbox property only available for those cases that have a "Manual" automation status
14. *[Muted case:](https://help.qase.io/en/articles/9217182-muted-tests)* checkbox marking tests as muted so their results will not affect the overall status of test runs where it can pass even if the muted test fails.

[![](https://downloads.intercomcdn.com/i/o/1099629346/bbf089ce98c83794ae02d39e/image.png?expires=1771427700&signature=8ee7c764ecf93dc84e40900cb6407e72be418179d51afd234324d1ba3582eef8&req=dSAuH898lIJbX%2FMW1HO4zdkj9e6EUVOR77R8%2FXor8bl1yNLQveNJPj%2BG%2BDwU%0ATarpZyJ1URjQhT9yvCg%3D%0A)](https://downloads.intercomcdn.com/i/o/1099629346/bbf089ce98c83794ae02d39e/image.png?expires=1771427700&signature=8ee7c764ecf93dc84e40900cb6407e72be418179d51afd234324d1ba3582eef8&req=dSAuH898lIJbX%2FMW1HO4zdkj9e6EUVOR77R8%2FXor8bl1yNLQveNJPj%2BG%2BDwU%0ATarpZyJ1URjQhT9yvCg%3D%0A)

System fields can be optionally switched on and off via the [fields section](https://help.qase.io/en/articles/6705423-workspace-management-fields). Click the "Configure fields" button and select the field you want to configure. Click on the “Enable for all projects button” and then configure:  
​

You can make your own [Custom Fields](https://help.qase.io/en/articles/5563701-custom-fields) with different data types to store extra information about your test cases not included in default properties. You won't find this field If you haven't created any Custom Fields yet.

### Conditions

Here, you can outline what needs to happen before conducting the Test Case (Pre-conditions) and the actions to be taken after the Test Case is completed (Post-conditions).

[![](https://downloads.intercomcdn.com/i/o/1099629981/a44c73c28da3a62c43bdc0f1/image.png?expires=1771427700&signature=253540e913f024803e5760625d593acd7d2f4ac146bee85fd0ae75243436248e&req=dSAuH898lIhXWPMW1HO4zSEk%2FTmDZsyt4h7wU5hP%2Fbi33tcbE5783NcCQ5hk%0AGF%2F0lt0IF%2B6Ibzt%2F8vk%3D%0A)](https://downloads.intercomcdn.com/i/o/1099629981/a44c73c28da3a62c43bdc0f1/image.png?expires=1771427700&signature=253540e913f024803e5760625d593acd7d2f4ac146bee85fd0ae75243436248e&req=dSAuH898lIhXWPMW1HO4zSEk%2FTmDZsyt4h7wU5hP%2Fbi33tcbE5783NcCQ5hk%0AGF%2F0lt0IF%2B6Ibzt%2F8vk%3D%0A)

### [Tags:](https://help.qase.io/en/articles/5563696-tags)

Tags are a quick way to label your test cases with values that don't require any preliminary configuration. This is a multi-select dropdown and is configured from your Workspace Settings.

[![](https://downloads.intercomcdn.com/i/o/1099633006/0b2598cc9a38b9dd76aee936/image.png?expires=1771427700&signature=d7a535e5654811ef36d31c1e27f60116f0c169299e5e409bdea9ae88cc5aebab&req=dSAuH899noFfX%2FMW1HO4zbSkfLNNrm6QcQKe8e5uLIfAWvVq1k5sE9QN%2Fq4U%0A53SkXW8q8AnGq0tXxbQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1099633006/0b2598cc9a38b9dd76aee936/image.png?expires=1771427700&signature=d7a535e5654811ef36d31c1e27f60116f0c169299e5e409bdea9ae88cc5aebab&req=dSAuH899noFfX%2FMW1HO4zbSkfLNNrm6QcQKe8e5uLIfAWvVq1k5sE9QN%2Fq4U%0A53SkXW8q8AnGq0tXxbQ%3D%0A)

### [Attachments](https://help.qase.io/en/articles/5563708-attachments):

Add clarity and additional context to your Test Case by uploading images, screenshots, video snippets, or other documents.

[![](https://downloads.intercomcdn.com/i/o/894519398/529f70cb6cca0e8fe7cd267b/image.png?expires=1771427700&signature=26ff1cb98544e76fd5b5736f8f52e435d5bbcc45af8703e6f51332d5e71cbbeb&req=fCkjE8h3nohXFb4f3HP0gDn5l7d75vGs5a3qJKGIavbn3CKRXpiUtWfIdHDT%0AVQC9Shj7iHLUD3IdPQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/894519398/529f70cb6cca0e8fe7cd267b/image.png?expires=1771427700&signature=26ff1cb98544e76fd5b5736f8f52e435d5bbcc45af8703e6f51332d5e71cbbeb&req=fCkjE8h3nohXFb4f3HP0gDn5l7d75vGs5a3qJKGIavbn3CKRXpiUtWfIdHDT%0AVQC9Shj7iHLUD3IdPQ%3D%3D%0A)

**NB:** There is a 128MB maximum size for a single file that can be attached.

### [Parameters](https://help.qase.io/en/articles/6640037-test-case-parameters):

You can set up your test case to be parametrized and run it through multiple iterations during a test run, depending on the parameter values you define.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304591749/ef25f9575794d71ee6a56dfbd25d/87453.png?expires=1771427700&signature=4f453230974318ab60d098dc6f509acd62991652c813be482619948d274e06fd&req=dSMnEsx3nIZbUPMW1HO4zXC5hH59ZTFrkZdH%2FOUY6Vm4MD915dDZ%2BHic7W4I%0AGMT7sc5o4CT9PJvREck%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304591749/ef25f9575794d71ee6a56dfbd25d/87453.png?expires=1771427700&signature=4f453230974318ab60d098dc6f509acd62991652c813be482619948d274e06fd&req=dSMnEsx3nIZbUPMW1HO4zXC5hH59ZTFrkZdH%2FOUY6Vm4MD915dDZ%2BHic7W4I%0AGMT7sc5o4CT9PJvREck%3D%0A)

You have the flexibility to add multiple parameters, each with multiple values.

Once you include a parametrized case in a test run, multiple instances of it will be added to the run, each representing a specific parameter value.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304593044/42e628c566e423b677d63dcc4202/53533.png?expires=1771427700&signature=d16df40606a2f76000582c66a1308c7c5eeea567ce04b2326c0b09989c8a8c97&req=dSMnEsx3noFbXfMW1HO4zbdaVlRxUgMFezUG8IGWemccJ2QNou6r3oRkZB5s%0Alrgr%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304593044/42e628c566e423b677d63dcc4202/53533.png?expires=1771427700&signature=d16df40606a2f76000582c66a1308c7c5eeea567ce04b2326c0b09989c8a8c97&req=dSMnEsx3noFbXfMW1HO4zbdaVlRxUgMFezUG8IGWemccJ2QNou6r3oRkZB5s%0Alrgr%0A)

## Test Case Steps

---

This section outlines the actions to be taken and the expected results for each step when executing a test case. For instance, when testing a software module offering GPS connectivity, you must specify the actions to perform and the anticipated outcomes.

There are two types of steps to pick from -

### a) Classic

[![](https://downloads.intercomcdn.com/i/o/934619102/6cbb5a146fcd562477a6885e/image.png?expires=1771427700&signature=51315591b35ce51df428b7f48adc240431a317d0528a572c21e1e8516590dfa1&req=fSMjEMh3nIFdFb4f3HP0gFcQS2Vhq56FbDthaf6RuP7A7b75ydpFeu9pfACz%0AL2LauWdiaGOPz6vw%2FA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/934619102/6cbb5a146fcd562477a6885e/image.png?expires=1771427700&signature=51315591b35ce51df428b7f48adc240431a317d0528a572c21e1e8516590dfa1&req=fSMjEMh3nIFdFb4f3HP0gFcQS2Vhq56FbDthaf6RuP7A7b75ydpFeu9pfACz%0AL2LauWdiaGOPz6vw%2FA%3D%3D%0A)

1. **Step Action:** A specific operation or task carried out within the test case step, such as interacting with an application interface or system.
2. **Data:** Input parameters or information utilized during the execution of a test, the influences the behavior of the system under test.

   * *This field can be disabled from the project's settings, under test case -> 'Dataset"*
3. **Expected Result:** The anticipated outcome or behavior that is considered correct for the given test case step.

### b) Gherkin

[![](https://downloads.intercomcdn.com/i/o/934618750/99196ae497327cfef89cdfa3/image.png?expires=1771427700&signature=ce75b12341327e22b27878407c1bc1d29b1c64e5c57387e6bfbfd20a1cfc0e5b&req=fSMjEMh2moRfFb4f3HP0gAkE%2B6TwO%2Fne0oBF2qisleFNgos5zY4re7k6UBe2%0ANQESO9DNFkOLvukBdA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/934618750/99196ae497327cfef89cdfa3/image.png?expires=1771427700&signature=ce75b12341327e22b27878407c1bc1d29b1c64e5c57387e6bfbfd20a1cfc0e5b&req=fSMjEMh2moRfFb4f3HP0gAkE%2B6TwO%2Fne0oBF2qisleFNgos5zY4re7k6UBe2%0ANQESO9DNFkOLvukBdA%3D%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/934618506/61c03a7f1056c79bc93e204d/image.png?expires=1771427700&signature=66764aeeff6c21a293d43062aa7edc44485a77436babf81530d119e34648a3ab&req=fSMjEMh2mIFZFb4f3HP0gNlhqCU%2B7KHtHap6lTWKJoWAUM18cZ5%2BfWuQqPkw%0Avk5mOgxrGEVrcIZIuA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/934618506/61c03a7f1056c79bc93e204d/image.png?expires=1771427700&signature=66764aeeff6c21a293d43062aa7edc44485a77436babf81530d119e34648a3ab&req=fSMjEMh2mIFZFb4f3HP0gNlhqCU%2B7KHtHap6lTWKJoWAUM18cZ5%2BfWuQqPkw%0Avk5mOgxrGEVrcIZIuA%3D%3D%0A)

Test Case can consist of several steps that must be performed; for every new step, hit the "**+ Add Step**" button on the bottom.  
​

[![](https://downloads.intercomcdn.com/i/o/894562269/31a74448abfbfb7c33e2a8f4/image.png?expires=1771427700&signature=ec69ebedfb500bd398239a9b276325ac8ec85e180c1b4afcdd02df6346714711&req=fCkjE898n4dWFb4f3HP0gKf5UFO7Y0D1I8SPGc03g2HDT0wDXxvw7bIpBRMr%0AVjq5fXrqXmCFgyvi9w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/894562269/31a74448abfbfb7c33e2a8f4/image.png?expires=1771427700&signature=ec69ebedfb500bd398239a9b276325ac8ec85e180c1b4afcdd02df6346714711&req=fCkjE898n4dWFb4f3HP0gKf5UFO7Y0D1I8SPGc03g2HDT0wDXxvw7bIpBRMr%0AVjq5fXrqXmCFgyvi9w%3D%3D%0A)

### Nested Steps

This is a list of sub-steps to be executed within a main step. This relationship forms a parent-child structure, where a step contains smaller steps within it.

To create a nested step, click on the three-dots menu of a step and select "Add child step."

[![](https://downloads.intercomcdn.com/i/o/934621810/51135041463a98e72d11049a/image.png?expires=1771427700&signature=481b8d28e86a92d8baf8f49a10a4a272b0a79aa94001e724dcba3c5838fbfdef&req=fSMjEMt%2FlYBfFb4f3HP0gGS9K6Q5IJSyngFNwgVLUstvfPrG485qs5aLIvJa%0AxItWapkRpavIzG2Zug%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/934621810/51135041463a98e72d11049a/image.png?expires=1771427700&signature=481b8d28e86a92d8baf8f49a10a4a272b0a79aa94001e724dcba3c5838fbfdef&req=fSMjEMt%2FlYBfFb4f3HP0gGS9K6Q5IJSyngFNwgVLUstvfPrG485qs5aLIvJa%0AxItWapkRpavIzG2Zug%3D%3D%0A)

### Shared Steps

To save time on repetitive tasks for Steps common to multiple Test Cases in a Project, consider creating Shared Steps.

Once you have at least one Shared Step in the "[Shared Steps](https://help.qase.io/en/articles/5563709-shared-steps)" view of your project, you'll find a "+ Add Shared Step" button when creating or editing a case.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304598057/db5bf44edc1768966fd75ab89431/image.png?expires=1771427700&signature=6651c9c97a14b5e55564d6eb587a06e93c3d1fe8e42a5a1da09713cf62771ec1&req=dSMnEsx3lYFaXvMW1HO4zQffZlL3%2BOVdbj5VPq%2FNYpSMxSWN0chxOA0bD6q4%0A3l3FwErmvwcIx%2F4ZMi0%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304598057/db5bf44edc1768966fd75ab89431/image.png?expires=1771427700&signature=6651c9c97a14b5e55564d6eb587a06e93c3d1fe8e42a5a1da09713cf62771ec1&req=dSMnEsx3lYFaXvMW1HO4zQffZlL3%2BOVdbj5VPq%2FNYpSMxSWN0chxOA0bD6q4%0A3l3FwErmvwcIx%2F4ZMi0%3D%0A)

When configuring a Case Step, you can customize it using the buttons beside the "Expected result" field:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304600045/53b40f516ecaf250dc1101970cc7/37590.png?expires=1771427700&signature=ac03932cb617920a6ee54d615bc700c343f073e76220752e8a343a455e8e953e&req=dSMnEs9%2BnYFbXPMW1HO4ze7ZRAGjyj2MNAG4LfQYnZld%2BdD26OrtgdASLJcS%0ApyLWPmeX3Q2nRYAnGXY%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304600045/53b40f516ecaf250dc1101970cc7/37590.png?expires=1771427700&signature=ac03932cb617920a6ee54d615bc700c343f073e76220752e8a343a455e8e953e&req=dSMnEs9%2BnYFbXPMW1HO4ze7ZRAGjyj2MNAG4LfQYnZld%2BdD26OrtgdASLJcS%0ApyLWPmeX3Q2nRYAnGXY%3D%0A)

1. You can create a Shared step / or turn a Shared step into a Regular step.
2. You can duplicate/clone a step.
3. You can edit a Shared step.
4. You can add a nested step.
5. You can delete a step,
6. You can attach files from your existing files in Qase or your computer.

## Quick edit from preview

---

All of the test case properties, including test case steps, description and preconditions can be edited directly from the preview.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554812512/150c8bb3ee0f2187cb539c7c13a4/quick+edit.gif?expires=1771427700&signature=3e809e8bbb2b3a043e25c6b3d2ad75535368249998882c979438af23cb0b6101&req=dSUiEsF%2Fn4ReW%2FMW1HO4zb98YKrJ5Kb8yY4LS30kjmVei9P47j0w0cDaVxX6%0Akon1BIXlPaeuirWsQ7o%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554812512/150c8bb3ee0f2187cb539c7c13a4/quick+edit.gif?expires=1771427700&signature=3e809e8bbb2b3a043e25c6b3d2ad75535368249998882c979438af23cb0b6101&req=dSUiEsF%2Fn4ReW%2FMW1HO4zb98YKrJ5Kb8yY4LS30kjmVei9P47j0w0cDaVxX6%0Akon1BIXlPaeuirWsQ7o%3D%0A)

## Test Case Actions

---

Once you have filled in all the information about your Test Case, you can:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304606696/a0a62ad9db1a48d9c2cc55220a02/12209.png?expires=1771427700&signature=894ffa7ea3aa1a33f809b290df04be421d16543b299e86a0b134c8d62b533c20&req=dSMnEs9%2Bm4dWX%2FMW1HO4zemIUb9oS0EYB2sQRmQLqTDPoDpWWrlHxw0EPARt%0ALcNPyj0%2Bl8pnepYk3gY%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304606696/a0a62ad9db1a48d9c2cc55220a02/12209.png?expires=1771427700&signature=894ffa7ea3aa1a33f809b290df04be421d16543b299e86a0b134c8d62b533c20&req=dSMnEs9%2Bm4dWX%2FMW1HO4zemIUb9oS0EYB2sQRmQLqTDPoDpWWrlHxw0EPARt%0ALcNPyj0%2Bl8pnepYk3gY%3D%0A)

* *[Send to review](https://help.qase.io/en/articles/5563713-test-case-review):* in this case, a new Test Case Review request will be created, and a person responsible for reviews will then decide on a submitted Test Case.
* *Save your Test Case*
* *Save and create another*
* *Cancel:* exit Test Case creation; your changes will not be saved.

### **Find your test case after saving:**

After saving the Test Case, it will be visible in your Repository structure alongside Test Suites and other Test Cases.

The Test Case will receive an automatically assigned code, combining the Project Code with a number (e.g., "DEMO-9," where "DEMO" is the project code, and "9" indicates the ninth Test Case created in this Project).

You can search your test cases using the code. Make sure to prefix the project code to the id.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554813003/5a3e31e908f3c2149df6524ab4af/80122.png?expires=1771427700&signature=fd066f99af6f0d35fb40319a5a158553da5970ab64eb11eeb0fe94e597d909b6&req=dSUiEsF%2FnoFfWvMW1HO4zVsWxO4YiIzmIE%2F7%2BDelGQrKV72jK3QTXBZ4nUCi%0As9KHdY3Pg%2FYhnCNGcJQ%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554813003/5a3e31e908f3c2149df6524ab4af/80122.png?expires=1771427700&signature=fd066f99af6f0d35fb40319a5a158553da5970ab64eb11eeb0fe94e597d909b6&req=dSUiEsF%2FnoFfWvMW1HO4zVsWxO4YiIzmIE%2F7%2BDelGQrKV72jK3QTXBZ4nUCi%0As9KHdY3Pg%2FYhnCNGcJQ%3D%0A)

When you click on a Test Case in the Repository view, a sidebar with a summary will appear on the right side of the screen.

You can view the Test Case properties and access options to Edit, Clone, or Delete it.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554814319/b1283ae2e67489ad69a80c31cb41/image.png?expires=1771427700&signature=8c72623c77b825cb5103d7e02c81ac2cc763c3fa7338cfd0f9b0d0b2dd6e2d83&req=dSUiEsF%2FmYJeUPMW1HO4zYPbwlaAAmyX6PQkAyhJjujEZo8D8GfZvyga31h%2F%0AMO4v65V6jTc4fYcJ9hg%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554814319/b1283ae2e67489ad69a80c31cb41/image.png?expires=1771427700&signature=8c72623c77b825cb5103d7e02c81ac2cc763c3fa7338cfd0f9b0d0b2dd6e2d83&req=dSUiEsF%2FmYJeUPMW1HO4zYPbwlaAAmyX6PQkAyhJjujEZo8D8GfZvyga31h%2F%0AMO4v65V6jTc4fYcJ9hg%3D%0A)

### **Restoring deleted cases:**

If you have deleted a Test Case, it will reside in the [Trash Bin](https://help.qase.io/en/articles/6628818-trash-bin) located in the three-dots-menu:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304617302/f46cacdb122ac5f413079633a510/44915.png?expires=1771427700&signature=a8c2ae85433823337b5d53329ca612b40f704cc42fc842cd92ed3d376afdd090&req=dSMnEs9%2FmoJfW%2FMW1HO4zQtMcT8yUjWKLFe7I17EPD2hn5RW1qhFhYxmVyYe%0AivTBV4ksaWX1VlV6JDw%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304617302/f46cacdb122ac5f413079633a510/44915.png?expires=1771427700&signature=a8c2ae85433823337b5d53329ca612b40f704cc42fc842cd92ed3d376afdd090&req=dSMnEs9%2FmoJfW%2FMW1HO4zQtMcT8yUjWKLFe7I17EPD2hn5RW1qhFhYxmVyYe%0AivTBV4ksaWX1VlV6JDw%3D%0A)

From the Trash Bin, you can restore a previously deleted Test case:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304618781/87e32cb60c91fd0cb8f4266fb143/56905.png?expires=1771427700&signature=263c17583a5ce7fe8ce553d4dffe92dbcd5008abed16ff5ff37dfd61764117b3&req=dSMnEs9%2FlYZXWPMW1HO4zacPouEbNFWMrmv6JbPyeAixRtlai36%2BEGtKCZBb%0AHfcEhzJC5NhqPJNESBY%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304618781/87e32cb60c91fd0cb8f4266fb143/56905.png?expires=1771427700&signature=263c17583a5ce7fe8ce553d4dffe92dbcd5008abed16ff5ff37dfd61764117b3&req=dSMnEs9%2FlYZXWPMW1HO4zacPouEbNFWMrmv6JbPyeAixRtlai36%2BEGtKCZBb%0AHfcEhzJC5NhqPJNESBY%3D%0A)

# Filters

---

When in the Repository view, you can apply Filters to find Test Cases with specific properties:

[![](https://downloads.intercomcdn.com/i/o/934640196/3232f5bdf14095832931ee5d/image.png?expires=1771427700&signature=f76e3821935724d56046fd873357b9cb925bfa62fec547937fa8754ec80db4c1&req=fSMjEM1%2BnIhZFb4f3HP0gNXq7JmB7R%2BqQngyk1LF9BozJm7lME4FuQyj1sGq%0AAfi3ifPf0%2FerQnreKg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/934640196/3232f5bdf14095832931ee5d/image.png?expires=1771427700&signature=f76e3821935724d56046fd873357b9cb925bfa62fec547937fa8754ec80db4c1&req=fSMjEM1%2BnIhZFb4f3HP0gNXq7JmB7R%2BqQngyk1LF9BozJm7lME4FuQyj1sGq%0AAfi3ifPf0%2FerQnreKg%3D%3D%0A)

In the example below, there are two filters applied - Cases that are of Normal severity and that are Manual:

[![](https://downloads.intercomcdn.com/i/o/934652945/28e823bb2e39bab45bba80ca/image.png?expires=1771427700&signature=3fd2eea5a64c8d895ab3844f68842b0a7294b902d337da0c22b126cb1db60b9b&req=fSMjEMx8lIVaFb4f3HP0gDzfnwID4P44OlFEBxqwTyl3dz2T0tDpk19xfF1T%0AK11vfPHlMI6WajHVVQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/934652945/28e823bb2e39bab45bba80ca/image.png?expires=1771427700&signature=3fd2eea5a64c8d895ab3844f68842b0a7294b902d337da0c22b126cb1db60b9b&req=fSMjEMx8lIVaFb4f3HP0gDzfnwID4P44OlFEBxqwTyl3dz2T0tDpk19xfF1T%0AK11vfPHlMI6WajHVVQ%3D%3D%0A)

# Search

---

You can look up a test case by its title, id, suite or any of it's fields' text.

Use the search box - start typing the name of a test case, and all the matching test cases will be shown:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554816721/8889bc894f9831ea0b1f37a0edaf/81484.png?expires=1771427700&signature=f2940f785489e1036a8dcc865b9c7012a20c904ae04b571f4d1ba09ab114c3cb&req=dSUiEsF%2Fm4ZdWPMW1HO4zaAsMKJe4I6OJkfIBObc0yJqT3al2OODKkU2xK4n%0Ar3wA0rs5Obmg6GZ7jjM%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554816721/8889bc894f9831ea0b1f37a0edaf/81484.png?expires=1771427700&signature=f2940f785489e1036a8dcc865b9c7012a20c904ae04b571f4d1ba09ab114c3cb&req=dSUiEsF%2Fm4ZdWPMW1HO4zaAsMKJe4I6OJkfIBObc0yJqT3al2OODKkU2xK4n%0Ar3wA0rs5Obmg6GZ7jjM%3D%0A)

# Bulk actions

---

Once you have multiple Test Cases, you can perform bulk edits. Check the boxes of several Test Cases to:

* Edit multiple cases' properties:

[![](https://downloads.intercomcdn.com/i/o/934670817/16aa860db20ad1b10f86431f/Jan-16-2024+19-47-41.gif?expires=1771427700&signature=66984e8adc21ffdccdf0c620d89a5e4750ccec631ae9f480a1b13eaad190b2f8&req=fSMjEM5%2BlYBYFb4f3HP0gF1LozmaaiwzG91tG6xmSs46jScB5AIhxw29uOBw%0An44tsIWX8RVcxkWPTw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/934670817/16aa860db20ad1b10f86431f/Jan-16-2024+19-47-41.gif?expires=1771427700&signature=66984e8adc21ffdccdf0c620d89a5e4750ccec631ae9f480a1b13eaad190b2f8&req=fSMjEM5%2BlYBYFb4f3HP0gF1LozmaaiwzG91tG6xmSs46jScB5AIhxw29uOBw%0An44tsIWX8RVcxkWPTw%3D%3D%0A)

* Perform an Express [Test Run](https://help.qase.io/en/articles/5563702-test-runs) of selected Test Cases:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304624228/bb21524c8f73e8d6e92a6cbc4ca8/run+cases.gif?expires=1771427700&signature=292aadc4cce62ad423836e04da4c1e06524b3ee41145afdbad53f8d40552bd32&req=dSMnEs98mYNdUfMW1HO4zSs2PLoqiZ%2BB5vyNHnglv8JdIyqxOwtNBgCFo1VN%0Akaws9jwO9uhbQ3kOxvQ%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304624228/bb21524c8f73e8d6e92a6cbc4ca8/run+cases.gif?expires=1771427700&signature=292aadc4cce62ad423836e04da4c1e06524b3ee41145afdbad53f8d40552bd32&req=dSMnEs98mYNdUfMW1HO4zSs2PLoqiZ%2BB5vyNHnglv8JdIyqxOwtNBgCFo1VN%0Akaws9jwO9uhbQ3kOxvQ%3D%0A)

* Delete Test Cases in bulk; when attempting to delete multiple Cases, you have to type "CONFIRM" into the field to prevent accidental deletion.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304626405/06c784f08e2222cebf3e413591c2/bulk+delete.gif?expires=1771427700&signature=b738640ad2b0c3013581c72c8dbb8f0ff6956bce317dad236bb7962ba738f741&req=dSMnEs98m4VfXPMW1HO4zZZk5fzS5QfQl2fLQ24Zoy%2BXIdaAbiaiyircAYtz%0AVwDvfO96cA%2BYCsF4hm4%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304626405/06c784f08e2222cebf3e413591c2/bulk+delete.gif?expires=1771427700&signature=b738640ad2b0c3013581c72c8dbb8f0ff6956bce317dad236bb7962ba738f741&req=dSMnEs98m4VfXPMW1HO4zZZk5fzS5QfQl2fLQ24Zoy%2BXIdaAbiaiyircAYtz%0AVwDvfO96cA%2BYCsF4hm4%3D%0A)

**NB**: This behavior is determined by a setting in project settings and can be switched on/off:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304628064/f830be6133f94a8df9be6c7f621b/76755.png?expires=1771427700&signature=9bf1c0ada4af10e69bfbf3c57cc482a6db5c4d2562d9815a682fd08655d44031&req=dSMnEs98lYFZXfMW1HO4zRzePg0qmIcedKab1kfs1rTuXHWhnp44W6h%2B4XD2%0AM6Z2%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304628064/f830be6133f94a8df9be6c7f621b/76755.png?expires=1771427700&signature=9bf1c0ada4af10e69bfbf3c57cc482a6db5c4d2562d9815a682fd08655d44031&req=dSMnEs98lYFZXfMW1HO4zRzePg0qmIcedKab1kfs1rTuXHWhnp44W6h%2B4XD2%0AM6Z2%0A)

---

Related Articles

[Export Test Cases](https://help.qase.io/en/articles/5563717-export-test-cases)[Webhooks](https://help.qase.io/en/articles/5563718-webhooks)[Import Test Cases](https://help.qase.io/en/articles/5563719-import-test-cases)[How to write effective test cases?](https://help.qase.io/en/articles/8680192-how-to-write-effective-test-cases)[Import - Replace matching test cases](https://help.qase.io/en/articles/12514198-import-replace-matching-test-cases)