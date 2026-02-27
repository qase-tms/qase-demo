# Defects

Defects in Qase, can help you keep track of the issues you've discovered, during the Test runs.

#

# Creating Defects

---

In Qase, there are two ways to create a defect:

1. You can create one from the defects section for any issue that is not necessarily connected to a particular test case or test run.
2. Another option is to file a defect upon failing a test case during a test run.

## **Option 1:** Filing a Defect from the *Defects* section of the workspace.

To do that, hit *Create New Defect,* and add all necessary details - Defect Title, Actual Result, Severity, fill out any [custom fields](https://help.qase.io/en/articles/5563701-custom-fields) applicable to Defects, and optionally add attachments:

[![](https://downloads.intercomcdn.com/i/o/1086753989/b1eb32f114b1ae096f89682b/image.png?expires=1771427700&signature=67eb16d05c567c5c05c15fa27920e26f10a26dcb63c8b9071ea6442ab975eb63&req=dSAvEM57nohXUPMW1HO4zRUFHTIttTALjd9cmaM%2FUCKWeiDqVoS%2BXUlOc8I8%0AbeJim5V0Hx0EsgIyi18%3D%0A)](https://downloads.intercomcdn.com/i/o/1086753989/b1eb32f114b1ae096f89682b/image.png?expires=1771427700&signature=67eb16d05c567c5c05c15fa27920e26f10a26dcb63c8b9071ea6442ab975eb63&req=dSAvEM57nohXUPMW1HO4zRUFHTIttTALjd9cmaM%2FUCKWeiDqVoS%2BXUlOc8I8%0AbeJim5V0Hx0EsgIyi18%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/1086757845/b15c74ad52b8ad9dcc393776/image.png?expires=1771427700&signature=879afbae201cd4a1db9e72331083abe82744425add5e4da50f6b58c0183f9a1a&req=dSAvEM57molbXPMW1HO4zT6ktSv7Yp9eaVFhFWjME2Fnx5Vb%2BzHqK4tv33Mb%0AaoW5vof8CGhqyvIsjl0%3D%0A)](https://downloads.intercomcdn.com/i/o/1086757845/b15c74ad52b8ad9dcc393776/image.png?expires=1771427700&signature=879afbae201cd4a1db9e72331083abe82744425add5e4da50f6b58c0183f9a1a&req=dSAvEM57molbXPMW1HO4zT6ktSv7Yp9eaVFhFWjME2Fnx5Vb%2BzHqK4tv33Mb%0AaoW5vof8CGhqyvIsjl0%3D%0A)

Such a defect would not have any reference to a [Test Case](https://help.qase.io/en/articles/5563704-test-cases) or a [Test Run](https://help.qase.io/en/articles/5563702-test-runs), since it has not been filed from any.

However, such a defect - just like a Defect filed during a Test Run - can be marked as "In Progress" (and then, consecutively, "Resolved") or Invalidated.

Additionally, the defect can also be linked with a external issue, like a Jira ticket.

[![](https://downloads.intercomcdn.com/i/o/1173277279/0aff84cc04cac368b4dc9ee7/link-defectssss.gif?expires=1771427700&signature=9ca8ecf11948d4c872d75126e83cb9dfb56023db5c1daf8e15392e3e2b377178&req=dSEgFct5moNYUPMW1HO4zcmTxaRL1XTm4mGimmUoDhIEaNX%2BWyfUVRdAGX8a%0Am%2Fue8Nb7I3YiBcKWl7s%3D%0A)](https://downloads.intercomcdn.com/i/o/1173277279/0aff84cc04cac368b4dc9ee7/link-defectssss.gif?expires=1771427700&signature=9ca8ecf11948d4c872d75126e83cb9dfb56023db5c1daf8e15392e3e2b377178&req=dSEgFct5moNYUPMW1HO4zcmTxaRL1XTm4mGimmUoDhIEaNX%2BWyfUVRdAGX8a%0Am%2Fue8Nb7I3YiBcKWl7s%3D%0A)

At the same time, any defects you will be filing during test runs later can be tied to an existing defect you created manually:

[![](https://downloads.intercomcdn.com/i/o/1086759914/5a7b7a1b5a6b974e4af5e038/defect+existing.gif?expires=1771427700&signature=7de6ef7b8c8c24e6ba677ed8b35eb5327a92e0fdc1d6ab0f8fa304e5fd2697cc&req=dSAvEM57lIheXfMW1HO4zSF1eemfNbwDO40YQJev1XXvTA%2F8Xzp%2BlLXQ710d%0A1t%2Fjka2AOh0bf%2FmSi%2Bc%3D%0A)](https://downloads.intercomcdn.com/i/o/1086759914/5a7b7a1b5a6b974e4af5e038/defect+existing.gif?expires=1771427700&signature=7de6ef7b8c8c24e6ba677ed8b35eb5327a92e0fdc1d6ab0f8fa304e5fd2697cc&req=dSAvEM57lIheXfMW1HO4zSF1eemfNbwDO40YQJev1XXvTA%2F8Xzp%2BlLXQ710d%0A1t%2Fjka2AOh0bf%2FmSi%2Bc%3D%0A)

This can be helpful when you are aware of the issues beforehand, even before performing a single test run, and want to document them in advance.

## **Option 2:** Filing a Defect when performing a test run

First off, when setting up your Project, keep in mind the "Fail case on step fail" setting:

[![](https://downloads.intercomcdn.com/i/o/1173278719/268688dcbbd903a60c835acf/image.png?expires=1771427700&signature=3e1300ce6d1a4f767f4cd8ec1d84dda83f6ebc1455248a778438357e57e2c418&req=dSEgFct5lYZeUPMW1HO4zYOl7Jq3vhI%2FRW%2FkGe8C01y%2F2ICsRdBDyvI0I2Cd%0AYTLdyjaUlJ5Ukgcy0f8%3D%0A)](https://downloads.intercomcdn.com/i/o/1173278719/268688dcbbd903a60c835acf/image.png?expires=1771427700&signature=3e1300ce6d1a4f767f4cd8ec1d84dda83f6ebc1455248a778438357e57e2c418&req=dSEgFct5lYZeUPMW1HO4zYOl7Jq3vhI%2FRW%2FkGe8C01y%2F2ICsRdBDyvI0I2Cd%0AYTLdyjaUlJ5Ukgcy0f8%3D%0A)

If this option is -

* **Enabled** - failing any single step in a case during a run will automatically fail an entire test case, and you will be suggested to file a new Defect.
* **Disabled** - failing a single step in a case will not result in failing an entire test case, and you will be able to continue with other steps in the run while being suggested to create a Defect only if you fail an entire test case.

So, how do we create a Defect during a test run?

* Mark a Test Case as "Failed", or add any other *Negative* Result:

[![](https://downloads.intercomcdn.com/i/o/1086762281/380dc2867790c133f7489c1e/image.png?expires=1771427700&signature=0a5fcaec5aa5a3ea5570f6d6b5ca27b61c144410bf98e833dce7bfa936445307&req=dSAvEM54n4NXWPMW1HO4zQAUQLSDOfgJavW5WJusMQBHhDK9RfbAysNI9iL5%0A%2F5FUj3E5wxze0QB1za0%3D%0A)](https://downloads.intercomcdn.com/i/o/1086762281/380dc2867790c133f7489c1e/image.png?expires=1771427700&signature=0a5fcaec5aa5a3ea5570f6d6b5ca27b61c144410bf98e833dce7bfa936445307&req=dSAvEM54n4NXWPMW1HO4zQAUQLSDOfgJavW5WJusMQBHhDK9RfbAysNI9iL5%0A%2F5FUj3E5wxze0QB1za0%3D%0A)

* You will be prompted to a Run result window, where you can file additional comment, record how much time was spent on a test case execution, attach files, and create/attach defect:

[![](https://downloads.intercomcdn.com/i/o/1086762654/d0b639275e31fe42e5b97ce1/image.png?expires=1771427700&signature=6903715070ec40f6c5c049615d5cf26f7fc17649268d8854a5d59122fd30e739&req=dSAvEM54n4daXfMW1HO4zdjuv5AP6tUnnakxtjWl6auE%2BvsYHQ94xhF89X%2Bx%0ABkjr3AIyDcfyrM9B1ZE%3D%0A)](https://downloads.intercomcdn.com/i/o/1086762654/d0b639275e31fe42e5b97ce1/image.png?expires=1771427700&signature=6903715070ec40f6c5c049615d5cf26f7fc17649268d8854a5d59122fd30e739&req=dSAvEM54n4daXfMW1HO4zdjuv5AP6tUnnakxtjWl6auE%2BvsYHQ94xhF89X%2Bx%0ABkjr3AIyDcfyrM9B1ZE%3D%0A)

* With the checkbox checked, you will be next prompted to fill out other remaining Defect properties, including any custom fields you created for it.   
  ​  
  You will be able to select whether you want to create a new Defect or attach an existing one to the issue you've found; change its title, severity, and custom fields' values; opt to send a connected issue to other [integrated third-party software systems](https://help.qase.io/en/collections/3564516-apps):

[![](https://downloads.intercomcdn.com/i/o/1086763725/7c23277887980cbc78219fc0/image.png?expires=1771427700&signature=ee926423bc1215056c2f3f7f6fb4a544ada50369d7696b53a0853a33f48a2d79&req=dSAvEM54noZdXPMW1HO4zUMlwcBhbJDDzDYXiTgzWRK9ui7%2BXzJrBzncq1eq%0Aj%2BjtyZ8Lzu3ZFPAYXEk%3D%0A)](https://downloads.intercomcdn.com/i/o/1086763725/7c23277887980cbc78219fc0/image.png?expires=1771427700&signature=ee926423bc1215056c2f3f7f6fb4a544ada50369d7696b53a0853a33f48a2d79&req=dSAvEM54noZdXPMW1HO4zUMlwcBhbJDDzDYXiTgzWRK9ui7%2BXzJrBzncq1eq%0Aj%2BjtyZ8Lzu3ZFPAYXEk%3D%0A)

Now a new Defect will be created from a test run result - you can find it saved under the "Defects" section and the “Defects” tab of your test run:

[![](https://downloads.intercomcdn.com/i/o/1086766364/9ce62f52316d813f5f16232a/image.png?expires=1771427700&signature=6f06637edd01a2bc882d9c9d21f860362dc9523c122bb09ac61022a197d09619&req=dSAvEM54m4JZXfMW1HO4zX%2BavRsQzi9mr5b5m6ZaCc%2B%2FkADPSF5qhDbncjHb%0AwpNmoTG0eRqMeRdl3Ds%3D%0A)](https://downloads.intercomcdn.com/i/o/1086766364/9ce62f52316d813f5f16232a/image.png?expires=1771427700&signature=6f06637edd01a2bc882d9c9d21f860362dc9523c122bb09ac61022a197d09619&req=dSAvEM54m4JZXfMW1HO4zX%2BavRsQzi9mr5b5m6ZaCc%2B%2FkADPSF5qhDbncjHb%0AwpNmoTG0eRqMeRdl3Ds%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/1086767382/731aab0dda7d67236f42f167/image.png?expires=1771427700&signature=7e4f37ac4c3467f85c73ec4afbfa9a4a84128e7a0f5c5bbdf549affb8349f24d&req=dSAvEM54moJXW%2FMW1HO4zVrKO1psuRDgNZ5se6UXYerX%2FXD685AdufjkyOHh%0ASjvLNQ97Wq8jDKyphzU%3D%0A)](https://downloads.intercomcdn.com/i/o/1086767382/731aab0dda7d67236f42f167/image.png?expires=1771427700&signature=7e4f37ac4c3467f85c73ec4afbfa9a4a84128e7a0f5c5bbdf549affb8349f24d&req=dSAvEM54moJXW%2FMW1HO4zVrKO1psuRDgNZ5se6UXYerX%2FXD685AdufjkyOHh%0ASjvLNQ97Wq8jDKyphzU%3D%0A)

**NB**: Defects viewed in a test run will show you only defects filed in that test run, but under the “Defects” section, you will find all defects filed in a project.

# Managing Defects

---

In the Defects section, you can search and filter all the defects filed in your project:

[![](https://downloads.intercomcdn.com/i/o/1086772137/0c83de6ad544b699ae149980/filter+defects.gif?expires=1771427700&signature=26f206521ed64d6dc26e33681947a036f2e460f6376b93b3157f170e5ce9ca1f&req=dSAvEM55n4BcXvMW1HO4zSxFkVFn%2BxIEHr6mW0qGuX9Gi8XSqPSHViJhBPte%0AvBs8Kqybp2%2Fo9bmAhFY%3D%0A)](https://downloads.intercomcdn.com/i/o/1086772137/0c83de6ad544b699ae149980/filter+defects.gif?expires=1771427700&signature=26f206521ed64d6dc26e33681947a036f2e460f6376b93b3157f170e5ce9ca1f&req=dSAvEM55n4BcXvMW1HO4zSxFkVFn%2BxIEHr6mW0qGuX9Gi8XSqPSHViJhBPte%0AvBs8Kqybp2%2Fo9bmAhFY%3D%0A)

Clicking on the Title of your new Defect will provide you with more details about this Defect, such as which Test Run it was performed in, which Test Case it pertains to, who reported this Defect - and other important data:

[![](https://downloads.intercomcdn.com/i/o/1086772894/538003089c5d0b0bc37e65ce/image.png?expires=1771427700&signature=c4c2e7646d66c7cd7cbd311e918b302e024195010828960f0f62b77511a5ba81&req=dSAvEM55n4lWXfMW1HO4zUNHHJWr7M9A2E7Y6QNEGEJ3TBppCq7KWM8OcWZG%0Aw4AcH%2BUCNE0njAzLWok%3D%0A)](https://downloads.intercomcdn.com/i/o/1086772894/538003089c5d0b0bc37e65ce/image.png?expires=1771427700&signature=c4c2e7646d66c7cd7cbd311e918b302e024195010828960f0f62b77511a5ba81&req=dSAvEM55n4lWXfMW1HO4zUNHHJWr7M9A2E7Y6QNEGEJ3TBppCq7KWM8OcWZG%0Aw4AcH%2BUCNE0njAzLWok%3D%0A)

After a Defect has been created, you can:

* Add a connected issue to other [integrated third-party software systems](https://help.qase.io/en/collections/3564516-apps). Here we have an example to connect a Jira issue:

[![](https://downloads.intercomcdn.com/i/o/1173238505/858d5f74fadc531142e98035/download+%282%29.gif?expires=1771427700&signature=4f5274227a27ce73ddfa8caf58c4996a27cde06ac4b47afc356461af57c7bb22&req=dSEgFct9lYRfXPMW1HO4zUSXdypoBZwoGc6wta%2B5Ijstafug4XpKkJcJMYF8%0AJh%2BK662x%2BF6HyVQibQQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1173238505/858d5f74fadc531142e98035/download+%282%29.gif?expires=1771427700&signature=4f5274227a27ce73ddfa8caf58c4996a27cde06ac4b47afc356461af57c7bb22&req=dSEgFct9lYRfXPMW1HO4zUSXdypoBZwoGc6wta%2B5Ijstafug4XpKkJcJMYF8%0AJh%2BK662x%2BF6HyVQibQQ%3D%0A)

* You can also change its status by marking it "In Progress" once you've started working on it

[![](https://downloads.intercomcdn.com/i/o/1086774703/452392a8e31f691485e979dc/in-pro.gif?expires=1771427700&signature=77ecf5d0abf40928abea34540cdc3b5782dd76591de3a11193e35bdc7f8255b8&req=dSAvEM55mYZfWvMW1HO4zdAxJ73MzwIsWR%2FSeuyxW2AEU0HSMXb7yIB4OHs5%0AWebZQyEGYx%2FKRe%2F63CU%3D%0A)](https://downloads.intercomcdn.com/i/o/1086774703/452392a8e31f691485e979dc/in-pro.gif?expires=1771427700&signature=77ecf5d0abf40928abea34540cdc3b5782dd76591de3a11193e35bdc7f8255b8&req=dSAvEM55mYZfWvMW1HO4zdAxJ73MzwIsWR%2FSeuyxW2AEU0HSMXb7yIB4OHs5%0AWebZQyEGYx%2FKRe%2F63CU%3D%0A)

* After the Defect has been marked as "In Progress", you can then mark it as "Resolved" once the issue has been fixed (at this stage, you can still invalidate it):

[![](https://downloads.intercomcdn.com/i/o/1086774841/00680310593e5abb1563132e/resolved.gif?expires=1771427700&signature=975a555a535a215218ab34f6b17ee73c11d6cb871dfeb7dd7f5cb2399a00db2c&req=dSAvEM55mYlbWPMW1HO4zbql4cazlspgbz7qr4EbYlb%2Bkm60oJb%2FcEXbVEww%0AbDpZjTcYqo%2FuLQd5UBA%3D%0A)](https://downloads.intercomcdn.com/i/o/1086774841/00680310593e5abb1563132e/resolved.gif?expires=1771427700&signature=975a555a535a215218ab34f6b17ee73c11d6cb871dfeb7dd7f5cb2399a00db2c&req=dSAvEM55mYlbWPMW1HO4zbql4cazlspgbz7qr4EbYlb%2Bkm60oJb%2FcEXbVEww%0AbDpZjTcYqo%2FuLQd5UBA%3D%0A)

* Invalidate it by updating its status to "Invalid", if, for example, an issue that's been filed is not really an issue:

[![](https://downloads.intercomcdn.com/i/o/1086776145/a65228ad5aa82a4294b24df1/invalid.gif?expires=1771427700&signature=b7a0acb44bf865f36406b3294f8e4a7119ecc26872a387ffb5403939ea28953f&req=dSAvEM55m4BbXPMW1HO4zaZ%2B8w23LE%2BMPcIAzMI3gGAMK0KwV0wOl1JJ2iGi%0As6nakZQ%2FtfNj6zShw3w%3D%0A)](https://downloads.intercomcdn.com/i/o/1086776145/a65228ad5aa82a4294b24df1/invalid.gif?expires=1771427700&signature=b7a0acb44bf865f36406b3294f8e4a7119ecc26872a387ffb5403939ea28953f&req=dSAvEM55m4BbXPMW1HO4zaZ%2B8w23LE%2BMPcIAzMI3gGAMK0KwV0wOl1JJ2iGi%0As6nakZQ%2FtfNj6zShw3w%3D%0A)

* Resolving a Defect will mark it as resolved, which will be made visible with a green icon to the left of a Defect's title. You can also apply filters in the Defects list view to look up specific Defects by parameters:

[![](https://downloads.intercomcdn.com/i/o/1086777342/0b0ae3d58c3785e63bbd6061/image.png?expires=1771427700&signature=7d9b41b07e1ee76eeac1937b957e8f30a1346ddde4bfeae633d3be4b5a15eb85&req=dSAvEM55moJbW%2FMW1HO4zVeSo%2FBShjMomFeWvCne2ZgZftxRJC7%2BwwUgzKW9%0AFjZFt1xRjR4KM3y3lVc%3D%0A)](https://downloads.intercomcdn.com/i/o/1086777342/0b0ae3d58c3785e63bbd6061/image.png?expires=1771427700&signature=7d9b41b07e1ee76eeac1937b957e8f30a1346ddde4bfeae633d3be4b5a15eb85&req=dSAvEM55moJbW%2FMW1HO4zVeSo%2FBShjMomFeWvCne2ZgZftxRJC7%2BwwUgzKW9%0AFjZFt1xRjR4KM3y3lVc%3D%0A)

You can introduce changes to a Defect as well by hitting the Edit button.

Editing a Defect will take you to another screen, where you can change the Defect's Title, enter the Actual Result, add an [attachment](https://help.qase.io/en/articles/5563708-attachments), etc., and update a defect once ready:

[![](https://downloads.intercomcdn.com/i/o/1086778925/4b07063ce3b09e9b86de6648/image.png?expires=1771427700&signature=045e9446cd9f3e7be6569884958829cf784d1718a5227a188c3de09bbda2b912&req=dSAvEM55lYhdXPMW1HO4zTObMEMQYFmSmL3eUxSujXEW%2BYtIusYaCSjgxNrT%0Ar9UbzlRPqNdygToP%2BqQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1086778925/4b07063ce3b09e9b86de6648/image.png?expires=1771427700&signature=045e9446cd9f3e7be6569884958829cf784d1718a5227a188c3de09bbda2b912&req=dSAvEM55lYhdXPMW1HO4zTObMEMQYFmSmL3eUxSujXEW%2BYtIusYaCSjgxNrT%0Ar9UbzlRPqNdygToP%2BqQ%3D%0A)

# Create or Link issues from external issue trackers

---

You can link your existing issues from any of the available issue tracker integration, or even create a new issue without having to leave Qase.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554792679/1efdd0ed73f361238d215da11e89/defects+link.gif?expires=1771427700&signature=de6b6fdc622fc2d77626febd3be8a1e1f1e28cfedef22d2662318f64b6782857&req=dSUiEs53n4dYUPMW1HO4zRhvkUb%2F1c7WxBaBHyj2tScRDvkHT%2BkBVCDCCIaX%0AVBfxnPvBQCoXdu%2BpYEo%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1554792679/1efdd0ed73f361238d215da11e89/defects+link.gif?expires=1771427700&signature=de6b6fdc622fc2d77626febd3be8a1e1f1e28cfedef22d2662318f64b6782857&req=dSUiEs53n4dYUPMW1HO4zRhvkUb%2F1c7WxBaBHyj2tScRDvkHT%2BkBVCDCCIaX%0AVBfxnPvBQCoXdu%2BpYEo%3D%0A)

---

Related Articles

[GitHub](https://help.qase.io/en/articles/6417206-github)[Asana](https://help.qase.io/en/articles/6417211-asana)[Jira Server/Datacenter Plugin installation](https://help.qase.io/en/articles/6417212-jira-server-datacenter-plugin-installation)[GitHub](https://help.qase.io/en/articles/7210938-github)[GitLab](https://help.qase.io/en/articles/7210982-gitlab)