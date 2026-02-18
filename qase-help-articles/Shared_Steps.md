# Shared Steps

**Shared steps** allows you to create a single step that can be shared across multiple test cases. This eliminates the need to recreate the same step manually for each test case and ensures consistency across all test cases in which the shared step is used.

Imagine that you have two different cases for a test suite - both require authorization into the internal system to proceed, so it will be one of the steps to recreate.

You could manually add an “Authorization” step to each test case individually, but it’s better to create a single shared step that you can consistently use across multiple test cases.

Shared steps are available both at a **project level**, and also at a **workspace level.**

## **Global Shared Steps (workspace-level)**

Global shared steps work much like regular shared steps, but they are available across every project in your workspace instead of being limited to just one.

For instance, you might be testing the same product on web, iOS, and Android. All these test cases may require the same action such as logging into the application.

Instead of creating the same shared step in each project, you can create one global shared step and use it wherever it is needed.

You can create a global (workspace-level) Shared step, from [workpsace >> shared steps](https://app.qase.io/workspace/shared-parameters).

[![Displaying Photo note](https://downloads.intercomcdn.com/i/o/wsaz8vex/2009065538/ad659d84342ebde0bccafb629e94/78384303-b8c6-4393-bf99-890375846a09?expires=1771427700&signature=95fd7be7adcac974a019ac999d4e5fa056a2df7f7eb8166f397c122f71f95847&req=diAnH8l4mIRcUfMW1HO4zQsLsV5xu6JPsbEdZrMoV8l96HRyZt0DDrTPFSEp%0AXUHwkA4KstcQoDexPDc%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/2009065538/ad659d84342ebde0bccafb629e94/78384303-b8c6-4393-bf99-890375846a09?expires=1771427700&signature=95fd7be7adcac974a019ac999d4e5fa056a2df7f7eb8166f397c122f71f95847&req=diAnH8l4mIRcUfMW1HO4zQsLsV5xu6JPsbEdZrMoV8l96HRyZt0DDrTPFSEp%0AXUHwkA4KstcQoDexPDc%3D%0A)

Please note that steps that already exist in test cases or shared steps within a project cannot be converted into global shared steps.

## Create a Shared step

Go to the **Shared Steps** section inside a project and create a new shared step

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304738847/a5d2069972b6bce9a7b7ade37d98/65158.png?expires=1771427700&signature=58ee264fa48289a59734508f4a2785031b08eecd8bc1d29e493f60d6c8152b89&req=dSMnEs59lYlbXvMW1HO4zWdIsgAqZu1xf%2F40WcDjISi%2BwX9YJL%2B62wvHF1nU%0AJ%2BOjoBeLetfSUGSROAM%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304738847/a5d2069972b6bce9a7b7ade37d98/65158.png?expires=1771427700&signature=58ee264fa48289a59734508f4a2785031b08eecd8bc1d29e493f60d6c8152b89&req=dSMnEs59lYlbXvMW1HO4zWdIsgAqZu1xf%2F40WcDjISi%2BwX9YJL%2B62wvHF1nU%0AJ%2BOjoBeLetfSUGSROAM%3D%0A)

Provide a title for your shared step to identify it easily.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304739995/e87607f3e0d5a5da74356471e909/90905.png?expires=1771427700&signature=1125fe04fe1da7b429128bae88de6e581e3547e49877edc5977adf8fcfb6248a&req=dSMnEs59lIhWXPMW1HO4zYcvG1pOpoIUj%2FTyCTMk9HIJT%2Bz4nhUvWy23RAOX%0ATKpgTTxoxlVtQiyVByg%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304739995/e87607f3e0d5a5da74356471e909/90905.png?expires=1771427700&signature=1125fe04fe1da7b429128bae88de6e581e3547e49877edc5977adf8fcfb6248a&req=dSMnEs59lIhWXPMW1HO4zYcvG1pOpoIUj%2FTyCTMk9HIJT%2Bz4nhUvWy23RAOX%0ATKpgTTxoxlVtQiyVByg%3D%0A)

A shared step can either be a single step or a group of multiple steps.

* Use the **+Add Step** button (located below the title field) to add individual steps, just like when creating steps for a test case.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304741842/72ab2d5b07b2a0bbe4d925a83451/38420.png?expires=1771427700&signature=d57a1deb797ad3c2a57bfb6088b7655cc509200273093e7eb6fedcdbfda4e6e6&req=dSMnEs56nIlbW%2FMW1HO4zSHPRnvKNEOY%2BAXRnF61wp3n3P9G664kG4%2FXnEg2%0ATvityRMssej9CsaeoTA%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304741842/72ab2d5b07b2a0bbe4d925a83451/38420.png?expires=1771427700&signature=d57a1deb797ad3c2a57bfb6088b7655cc509200273093e7eb6fedcdbfda4e6e6&req=dSMnEs56nIlbW%2FMW1HO4zSHPRnvKNEOY%2BAXRnF61wp3n3P9G664kG4%2FXnEg2%0ATvityRMssej9CsaeoTA%3D%0A)

It is currently not possible create nested steps inside of a shared step.

##

## Bulk Actions

You can take two bulk actions for shared steps within the project:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/2009039527/638711c18a14a13c99b239876350/97010.png?expires=1771427700&signature=3c3c00c64eb9f5560088ed85cc40da0e828904c9fbd926b2aa4bf6d8fbd009a8&req=diAnH8l9lIRdXvMW1HO4zbRlncXKYRlteEUNmOWOJqO2h4I8%2BMJ7GG9Zu5Db%0AJBP2RbEyT6q%2FKvvh4OQ%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/2009039527/638711c18a14a13c99b239876350/97010.png?expires=1771427700&signature=3c3c00c64eb9f5560088ed85cc40da0e828904c9fbd926b2aa4bf6d8fbd009a8&req=diAnH8l9lIRdXvMW1HO4zbRlncXKYRlteEUNmOWOJqO2h4I8%2BMJ7GG9Zu5Db%0AJBP2RbEyT6q%2FKvvh4OQ%3D%0A)

1. Convert the selected shared steps into global shared steps. Please note that this action is irreversible. Use caution, as project-level shared steps will be converted to workspace-level shared steps, making them accessible to all team members.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/2009045001/a81938e59a760322284244a82f58/6032.png?expires=1771427700&signature=5c11edaf08b2ef7a74d2c1a1b2f3cb885dc429f89496406ee38622e60c070677&req=diAnH8l6mIFfWPMW1HO4zRdkWnIeBRRnV1mRe0DuKPSU2of36HUGLspR%2BFKt%0AsKq60aL36b%2BBzKd5FPo%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/2009045001/a81938e59a760322284244a82f58/6032.png?expires=1771427700&signature=5c11edaf08b2ef7a74d2c1a1b2f3cb885dc429f89496406ee38622e60c070677&req=diAnH8l6mIFfWPMW1HO4zRdkWnIeBRRnV1mRe0DuKPSU2of36HUGLspR%2BFKt%0AsKq60aL36b%2BBzKd5FPo%3D%0A)

2. Delete select shared steps. You can choose between permanently deleting all the steps where the shared steps are used, in test cases. Or, convert those steps into local regular steps before deletion.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/2009048423/2ee36b064139189dfaf483ab1ea8/80617.png?expires=1771427700&signature=ac883114c54514d6a496d12d2968539d512e9225ff5e2a6e7248c987cb2447b7&req=diAnH8l6lYVdWvMW1HO4zZAb3n5bfPI4%2BcwgHj58p4JbGyakiXTbZBK%2FOOwL%0ACVf%2Br753BSxqlpHCKco%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/2009048423/2ee36b064139189dfaf483ab1ea8/80617.png?expires=1771427700&signature=ac883114c54514d6a496d12d2968539d512e9225ff5e2a6e7248c987cb2447b7&req=diAnH8l6lYVdWvMW1HO4zZAb3n5bfPI4%2BcwgHj58p4JbGyakiXTbZBK%2FOOwL%0ACVf%2Br753BSxqlpHCKco%3D%0A)

For Global shared steps, you can select multiple test cases to delete at once. You'll have the same two options as project level shared steps, when deleting.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/2009060276/fafcf641b939ae7dc00d54e4bab6/16789.png?expires=1771427700&signature=c695bdc286f8841bdac637aaee5b4536e0f8b8f6e130c3e3391ddc4603669c6a&req=diAnH8l4nYNYX%2FMW1HO4zfM4D9xjmqGfBMZulTPOMGzyHOBz4h89usc%2FmSfg%0AFoTEEyRqoeOxA2NGtro%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/2009060276/fafcf641b939ae7dc00d54e4bab6/16789.png?expires=1771427700&signature=c695bdc286f8841bdac637aaee5b4536e0f8b8f6e130c3e3391ddc4603669c6a&req=diAnH8l4nYNYX%2FMW1HO4zfM4D9xjmqGfBMZulTPOMGzyHOBz4h89usc%2FmSfg%0AFoTEEyRqoeOxA2NGtro%3D%0A)

## Convert a existing local step into Shared step:

While editing a test case, you can convert a regular step into a shared step. Adjust the newly created shared step later in the **Shared Steps** section.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1861043625/f1bc3db12be2fcb10d5509d10f39/convert%2Bshared%2Bstep.gif?expires=1771427700&signature=25da3c05741bfc83acc0fba8136a9ce7251d116ecadbf920b49b5cc5fad2f4d5&req=dSghF8l6noddXPMW1HO4zbrcz7GnV771lTAA%2FfLIhY30aNJELilAufLUZEGJ%0AdhoxwxsyF0o5ZWKnMCA%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1861043625/f1bc3db12be2fcb10d5509d10f39/convert%2Bshared%2Bstep.gif?expires=1771427700&signature=25da3c05741bfc83acc0fba8136a9ce7251d116ecadbf920b49b5cc5fad2f4d5&req=dSghF8l6noddXPMW1HO4zbrcz7GnV771lTAA%2FfLIhY30aNJELilAufLUZEGJ%0AdhoxwxsyF0o5ZWKnMCA%3D%0A)

## Add Shared step to a test case:

When you create or edit a test case, select the **Add Shared Step** button to include either a project-level shared step or a global shared step.

You can preview a step before adding it to the test case.

Global shared steps have a 🌐 icon at the beginning so you can tell them apart.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1861052612/2a1fe173e3d5841187636819e8dc/shared+steps+global+add.gif?expires=1771427700&signature=9506490b6a617b2a4bb4e8f82a4a3cd5e9b8920ea6dd7e143b88d1574854925a&req=dSghF8l7n4deW%2FMW1HO4zeZ94trbbclJq6OrzWUVxLPaXOJQxABdtEulfA7M%0AY876rpajDzeZ3DqLRbc%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1861052612/2a1fe173e3d5841187636819e8dc/shared+steps+global+add.gif?expires=1771427700&signature=9506490b6a617b2a4bb4e8f82a4a3cd5e9b8920ea6dd7e143b88d1574854925a&req=dSghF8l7n4deW%2FMW1HO4zeZ94trbbclJq6OrzWUVxLPaXOJQxABdtEulfA7M%0AY876rpajDzeZ3DqLRbc%3D%0A)

## Editing Shared steps:

You can update the shared step or global shared steps by selecting the Edit button in the Shared Steps section.

*Any changes you make and save will automatically apply to every test case that uses that shared step, which helps keep everything consistent and up to date.*

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304746119/0f00e9e5ff681c6d18ad0a8c949d/modify+shared+step.gif?expires=1771427700&signature=015a9d2e560e16ebbadc7f07d19d42e1eb472504d28f891529f11f64dbed69ca&req=dSMnEs56m4BeUPMW1HO4zRTqHNcgn42ne%2FeX1I9CHJPF%2BXUNMXeMihWFs6S9%0Ays%2BTgavppkrlj2uypqY%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304746119/0f00e9e5ff681c6d18ad0a8c949d/modify+shared+step.gif?expires=1771427700&signature=015a9d2e560e16ebbadc7f07d19d42e1eb472504d28f891529f11f64dbed69ca&req=dSMnEs56m4BeUPMW1HO4zRTqHNcgn42ne%2FeX1I9CHJPF%2BXUNMXeMihWFs6S9%0Ays%2BTgavppkrlj2uypqY%3D%0A)

## View linked test cases.

For both shared steps, within project and global – you can view the test cases the step is used in by.

For shared steps within a project, clicking the links in the ‘Attached to’ column will open the repository and show all the test cases where that step is used.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1804188555/ed899c5a1160e0f9081e9b3cc4d6/image.png?expires=1771427700&signature=9225b6c7321aa7b0cea00991790dc352bb9e1737276a937807fa83de96784492&req=dSgnEsh2lYRaXPMW1HO4zU0iQEBqLGF23Gb%2FVBMhxBD8Mfcw01agbvHzBxde%0ASEAqb5pwnLyJkp1rwiw%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1804188555/ed899c5a1160e0f9081e9b3cc4d6/image.png?expires=1771427700&signature=9225b6c7321aa7b0cea00991790dc352bb9e1737276a937807fa83de96784492&req=dSgnEsh2lYRaXPMW1HO4zU0iQEBqLGF23Gb%2FVBMhxBD8Mfcw01agbvHzBxde%0ASEAqb5pwnLyJkp1rwiw%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1804189388/bb70eac5c2a57f0bdb374476b30c/image.png?expires=1771427700&signature=bd3b2be7a0a23ade1215ca4cd960d8bc977617f43d6f5264531f413cd2c98245&req=dSgnEsh2lIJXUfMW1HO4za4THozp8BiV%2FoGVnL0SEaj6dfqiHmISdjMMxQp9%0AmyXVzcyTLo3Ues7L4z0%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1804189388/bb70eac5c2a57f0bdb374476b30c/image.png?expires=1771427700&signature=bd3b2be7a0a23ade1215ca4cd960d8bc977617f43d6f5264531f413cd2c98245&req=dSgnEsh2lIJXUfMW1HO4za4THozp8BiV%2FoGVnL0SEaj6dfqiHmISdjMMxQp9%0AmyXVzcyTLo3Ues7L4z0%3D%0A)

For Global shared steps, since they can be linked to multiple projects, you can view all repositories that use the step.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1875141927/ca959c7efdaf53042734ffda8e94/57585.png?expires=1771427700&signature=75d977c52d7c23b9986071b42d683d4441d6be45f33d87ea0d750ea441ee58e2&req=dSggE8h6nIhdXvMW1HO4zSfqwF%2FO2HvolJMjG3S%2FPKesaFDszZUmzGn2NDfe%0ANlfRcFRfhpvPacKoymw%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1875141927/ca959c7efdaf53042734ffda8e94/57585.png?expires=1771427700&signature=75d977c52d7c23b9986071b42d683d4441d6be45f33d87ea0d750ea441ee58e2&req=dSggE8h6nIhdXvMW1HO4zSfqwF%2FO2HvolJMjG3S%2FPKesaFDszZUmzGn2NDfe%0ANlfRcFRfhpvPacKoymw%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1875142343/48b372dd9ed6766d36aa10f4fba8/image.png?expires=1771427700&signature=ad54a108a1727da2fd3403c2685fbfdf3177a7bc79d955b33df03da81b7b08f1&req=dSggE8h6n4JbWvMW1HO4zWE9Gce7TYSUQUhNhrFvB8bfz9Yf4Itxshp5zur0%0AuN4WoVJj74tqG0u5zuo%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1875142343/48b372dd9ed6766d36aa10f4fba8/image.png?expires=1771427700&signature=ad54a108a1727da2fd3403c2685fbfdf3177a7bc79d955b33df03da81b7b08f1&req=dSggE8h6n4JbWvMW1HO4zWE9Gce7TYSUQUhNhrFvB8bfz9Yf4Itxshp5zur0%0AuN4WoVJj74tqG0u5zuo%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1875142862/3806924329ce77fd5ab92338f760/20603.png?expires=1771427700&signature=2c72021fab9da03ca508653844e3f2ec39ad2bc8a4bb3cf1e3c7b7daf5e92646&req=dSggE8h6n4lZW%2FMW1HO4zcEzBTVXQXNqFhzV70LdMKIaISTRWCYY8rl0MaR9%0A7k0%2BBOyO1834Hr4z89U%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1875142862/3806924329ce77fd5ab92338f760/20603.png?expires=1771427700&signature=2c72021fab9da03ca508653844e3f2ec39ad2bc8a4bb3cf1e3c7b7daf5e92646&req=dSggE8h6n4lZW%2FMW1HO4zcEzBTVXQXNqFhzV70LdMKIaISTRWCYY8rl0MaR9%0A7k0%2BBOyO1834Hr4z89U%3D%0A)

## Cloning Shared steps:

You can easily create a copy of the shared steps (*both project level and global)* by cloning the step. You can edit the new step's title before cloning.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1875146824/8d0f15133d8a79340c64b3c3bd9d/17310.png?expires=1771427700&signature=47a56c21eabddc1ae9961003ff0caf16d594efa27cd922e54f84e790c38f8bbc&req=dSggE8h6m4ldXfMW1HO4ze3S3C%2FSIQBmsHUIqSYPngf1B5QPfYp0hBDAMO3s%0ANTwbQqR3t9Yi04nPLgM%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1875146824/8d0f15133d8a79340c64b3c3bd9d/17310.png?expires=1771427700&signature=47a56c21eabddc1ae9961003ff0caf16d594efa27cd922e54f84e790c38f8bbc&req=dSggE8h6m4ldXfMW1HO4ze3S3C%2FSIQBmsHUIqSYPngf1B5QPfYp0hBDAMO3s%0ANTwbQqR3t9Yi04nPLgM%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1875149039/a7fcf2c41dd2f89e44681bfd769e/70949.png?expires=1771427700&signature=0fb3ccdfcd2c84f6a70e5280ad064868fd31e11c6a11747fc722faefb0f9642e&req=dSggE8h6lIFcUPMW1HO4zdkkxWjIbSnRlhRrsxBUrkJpLFPM87ViMxDAmody%0AD%2FgVyMckecEds9KTr3w%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1875149039/a7fcf2c41dd2f89e44681bfd769e/70949.png?expires=1771427700&signature=0fb3ccdfcd2c84f6a70e5280ad064868fd31e11c6a11747fc722faefb0f9642e&req=dSggE8h6lIFcUPMW1HO4zdkkxWjIbSnRlhRrsxBUrkJpLFPM87ViMxDAmody%0AD%2FgVyMckecEds9KTr3w%3D%0A)

---

Related Articles

[Tags](https://help.qase.io/en/articles/5563696-tags)[Test Cases](https://help.qase.io/en/articles/5563704-test-cases)[Projects](https://help.qase.io/en/articles/5563706-projects)[Startup plan](https://help.qase.io/en/articles/5563728-startup-plan)[Test Case Parameters](https://help.qase.io/en/articles/6640037-test-case-parameters)