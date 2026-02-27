# Test Case Parameters

# Overview

---

In your testing process, **Parameters** allow you to capture variables that can be reused across multiple executions of the same [Test Case](https://help.qase.io/en/articles/5563704-test-cases). This eliminates the need to create separate test cases or duplicate steps for different conditions.

# How Parameters help?

---

Consider a scenario where you need to test the sign-in functionality of a web application under various conditions. For each user, you’ll need to test each website twice under different conditions (VPN, WiFi, HTTPS, SSO, Cookies), both enabled and disabled.

**Parameter 1**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Browser | Chromium | Firefox | Safari | Microsoft Edge |

**Parameter 2**

|  |  |  |  |
| --- | --- | --- | --- |
| Website | qase.io | blog.qase.io | help.qase.io |

Group 1 is a **Secure network**; Group 2 is an **In-secure network**.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| is on VPN? | is on WiFi? | is HTTPS? | Using SSO? | Cookies Accepted? |
| Yes | No | Yes | No | Yes |
| No | Yes | No | Yes | No |

## Create a test case with Parameters -

---

Go to your repository, to select an existing test case, or create a new one.

[![](https://downloads.intercomcdn.com/i/o/1092478621/057cb6a83cc356629396cbbe/image.png?expires=1771427700&signature=0b446f9ae01bb697574e0923b9d081bccdfdcfa22eddbc64a7c28118ed7bf035&req=dSAuFM15lYddWPMW1HO4zRTGkPEdku8XZKsG%2BQV157sYJOGgs6YE7RRHW6Hy%0AQ1KR%2FdZHbZjCoSM5J3Q%3D%0A)](https://downloads.intercomcdn.com/i/o/1092478621/057cb6a83cc356629396cbbe/image.png?expires=1771427700&signature=0b446f9ae01bb697574e0923b9d081bccdfdcfa22eddbc64a7c28118ed7bf035&req=dSAuFM15lYddWPMW1HO4zRTGkPEdku8XZKsG%2BQV157sYJOGgs6YE7RRHW6Hy%0AQ1KR%2FdZHbZjCoSM5J3Q%3D%0A)

--

[![](https://downloads.intercomcdn.com/i/o/1158941641/08a0030df0eb9849d41e94a2/image.png?expires=1771427700&signature=c2ce3e820ba9dc33446b31717d3e52c172e8c30abf752ce55e9b6f1f27b0e6c8&req=dSEiHsB6nIdbWPMW1HO4zYM7ewuJK8PYkVQp1FqmdOqOhIMogtRw10C%2BAmum%0AvMRFRiMV4pnVXQSzIq4%3D%0A)](https://downloads.intercomcdn.com/i/o/1158941641/08a0030df0eb9849d41e94a2/image.png?expires=1771427700&signature=c2ce3e820ba9dc33446b31717d3e52c172e8c30abf752ce55e9b6f1f27b0e6c8&req=dSEiHsB6nIdbWPMW1HO4zYM7ewuJK8PYkVQp1FqmdOqOhIMogtRw10C%2BAmum%0AvMRFRiMV4pnVXQSzIq4%3D%0A)

When you either create or edit an existing test case, you can scroll down to find the "Parameters" section and simply click on the "+ Add Parameter' button.

[![](https://downloads.intercomcdn.com/i/o/1158942851/e1a0e84ed1f9e1dceebc0420/image.png?expires=1771427700&signature=399391ade595088af6bf047e0f21379dc68bfbac2057b5ffc40edc2c174ade4d&req=dSEiHsB6n4laWPMW1HO4zSsAoLmqvruXqKFWX8bO2rRM0GNYlyf4xNnIkoqt%0AUVem%2FeCBVkkPkCOrGXM%3D%0A)](https://downloads.intercomcdn.com/i/o/1158942851/e1a0e84ed1f9e1dceebc0420/image.png?expires=1771427700&signature=399391ade595088af6bf047e0f21379dc68bfbac2057b5ffc40edc2c174ade4d&req=dSEiHsB6n4laWPMW1HO4zSsAoLmqvruXqKFWX8bO2rRM0GNYlyf4xNnIkoqt%0AUVem%2FeCBVkkPkCOrGXM%3D%0A)

**Then,** proceed to add the following test case steps

* Check the network condition specified (Secure/ Insecure)
* Launch the specified browser.
* Navigate to the specified website.
* Enter the login credentials for the specified site.
* Click the "Sign In" button.

# Executing a Parameterized test case -

---

When a test case with Parameters is included in a test run, it generates multiple instances of the test case, each corresponding to a specific combination of parameter values.

[![](https://downloads.intercomcdn.com/i/o/1158945835/7d26d78149b95f35931c896a/param+222.gif?expires=1771427700&signature=02b9c76665ee9c92917d45e591e03053c6b305cf0c7c19af4b9d2afee6c67e5a&req=dSEiHsB6mIlcXPMW1HO4zdQWL7U%2FFJY3b8zaUu6TvIhpLKOQ35nkLSf3Ny1W%0Anj2n2OAv0fsP9JPl7QU%3D%0A)](https://downloads.intercomcdn.com/i/o/1158945835/7d26d78149b95f35931c896a/param+222.gif?expires=1771427700&signature=02b9c76665ee9c92917d45e591e03053c6b305cf0c7c19af4b9d2afee6c67e5a&req=dSEiHsB6mIlcXPMW1HO4zdQWL7U%2FFJY3b8zaUu6TvIhpLKOQ35nkLSf3Ny1W%0Anj2n2OAv0fsP9JPl7QU%3D%0A)

For example:

* Test 1: Browser = `Chromium`, Website = `https://www.qase.io`, Secure = `VPN = Yes, WiFi = Yes, HTTPS = Yes, SSO = Yes, Cookies = Yes`  
  ​
* Test 2: Browser = `Chromium`, Website = `https://blog.qase.io`, Secure = `VPN = Yes, WiFi = Yes, HTTPS = Yes, SSO = Yes, Cookies = Yes`

(and so on, until all combinations are covered)

* Test 24: Browser = `Microsoft Edge`, Website = `https://help.qase.io`, Insecure = `VPN = Yes, WiFi = Yes, HTTPS = Yes, SSO = Yes, Cookies = Yes`

With single parameters, the total number of test cases is the product of the number of values for each parameter. For example, with two parameters having 3 and 4 values, you get (3\*4) 12 test cases.

Given the network security conditions (Secured and Unsecured), it’s impractical to list each component as a separate parameter. Instead, all components are either enabled in a secured network or disabled in an unsecured network. This is where Parameter Groups become useful.

## How is a Parameter group different from a single parameter?

To further streamline the testing process, you can group related parameters into "Parameter Groups." For example:

* **Network security:** Is on VPN, Is on WiFi, Is HTTPS, SSO sign-in, Cookies enabled
* **Account status:** is Active; has a custom role; is a regular user, is Owner

Parameter Groups are useful when not all combinations of parameters are relevant or meaningful. For instance, with “Account Status” parameter, a combination of “not active” and “not Owner” might not exist in your system or be applicable.

In such cases, Parameter Groups help you focus only on practical and realistic combinations, eliminating unnecessary tests. This ensures that your testing is efficient and covers only meaningful scenarios.

In our example, although we initially had 12 combinations for the single parameters, each of these needs to be tested on both Secure and Insecure network groups. As a result, the total number of test cases in the run will now be 24.

In a test run, the total number of parameter combinations for a case cannot exceed **1,024**.

## **Find your parameter siblings from the Run wizard**

In the Test Run dashboard, selecting a parameterized test case will display a ‘**siblings**’ tab. This tab shows copies of the test case for all other parameter values associated with the selected case.

[![](https://downloads.intercomcdn.com/i/o/1093639940/3232153bb1972d5890876066/image.png?expires=1771427700&signature=e527aaa995d4d18d3731a1b6167db8593529e18fc28f86407bf5e62208e3b27d&req=dSAuFc99lIhbWfMW1HO4zUJB7BYSxe%2FVY4HWheA%2Bkqai5NS%2BaI1EYgmIACLw%0AmnBpKGk3tk6oa5h9oh0%3D%0A)](https://downloads.intercomcdn.com/i/o/1093639940/3232153bb1972d5890876066/image.png?expires=1771427700&signature=e527aaa995d4d18d3731a1b6167db8593529e18fc28f86407bf5e62208e3b27d&req=dSAuFc99lIhbWfMW1HO4zUJB7BYSxe%2FVY4HWheA%2Bkqai5NS%2BaI1EYgmIACLw%0AmnBpKGk3tk6oa5h9oh0%3D%0A)

# Shared Parameters

Shared Parameters allow you to create reusable parameters at the workspace level that can be applied across multiple test cases and projects. Instead of creating the same parameters repeatedly in individual test cases, you can now define them once and share them wherever needed.

If you change a shared parameter, these changes will automatically apply to all test cases using this parameter.

## Creating Shared Parameters

1. From the workspace , go to "Shared Parameters" and create your Single or Group shared parameters.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1657992629/a5248d070c8f8ebac51fd296f93b/image.png?expires=1771427700&signature=bece289e6c24c7f176514dfda60ccee525f44cffda9263aa51edf2265e885798&req=dSYiEcB3n4ddUPMW1HO4zRpa8rFMonzUmj%2BlKsQefeWkyrO9w9sVWWx3MM4C%0AytPU%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1657992629/a5248d070c8f8ebac51fd296f93b/image.png?expires=1771427700&signature=bece289e6c24c7f176514dfda60ccee525f44cffda9263aa51edf2265e885798&req=dSYiEcB3n4ddUPMW1HO4zRpa8rFMonzUmj%2BlKsQefeWkyrO9w9sVWWx3MM4C%0AytPU%0A)
2. You can select which projects should have access to this shared parameter  
   ​

   [![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1657993435/155ff506b5abb9b651eef3f62cfe/image.png?expires=1771427700&signature=73ad75cc919e562a73363a3172d91ffffa76bfcb35b1fd07e64bf56e94802064&req=dSYiEcB3noVcXPMW1HO4zfUukYm6%2FiyNByNQoLowN1927ogMLd1E0hFsvq1n%0AMUSt%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1657993435/155ff506b5abb9b651eef3f62cfe/image.png?expires=1771427700&signature=73ad75cc919e562a73363a3172d91ffffa76bfcb35b1fd07e64bf56e94802064&req=dSYiEcB3noVcXPMW1HO4zfUukYm6%2FiyNByNQoLowN1927ogMLd1E0hFsvq1n%0AMUSt%0A)
3. And, save your shared parameter

Once created, you'll see your shared parameters listed with the following information:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1657993811/ecd34d69660f3dfc84d582efde93/image.png?expires=1771427700&signature=f62aa9c1dcdeb3a98ec893b14fd1718c71eaf76f3f932389ba864da1c323cfe0&req=dSYiEcB3noleWPMW1HO4zTWYHE6waVKJYDBRwH39k%2FzNdlhxbgta6jtrWkM5%0AB4ZMaLgdZY%2B7DibRodM%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1657993811/ecd34d69660f3dfc84d582efde93/image.png?expires=1771427700&signature=f62aa9c1dcdeb3a98ec893b14fd1718c71eaf76f3f932389ba864da1c323cfe0&req=dSYiEcB3noleWPMW1HO4zTWYHE6waVKJYDBRwH39k%2FzNdlhxbgta6jtrWkM5%0AB4ZMaLgdZY%2B7DibRodM%3D%0A)

* Parameter name and type (single or group)
* Which projects have access
* Number of test cases currently using the parameter

## Attaching Shared Parameters to Test Cases

When editing or creating a test case, you'll notice the Parameters section now includes separate options:

* Single Parameters (local to the test case)
* Group Parameters (local to the test case)
* Shared Parameters (workspace-level parameters)

  [![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1657994425/2b5e5a204fe72abadde3396a20fc/image.png?expires=1771427700&signature=c855aeabf9e489ddfaeed3adcab6220e552d83a474f0e901de4f4e32330e052f&req=dSYiEcB3mYVdXPMW1HO4zYzN4Gxb%2F%2FMB%2Fm5EOLgRmEINCXRmjJRYQYB3M74j%0ApwXS%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1657994425/2b5e5a204fe72abadde3396a20fc/image.png?expires=1771427700&signature=c855aeabf9e489ddfaeed3adcab6220e552d83a474f0e901de4f4e32330e052f&req=dSYiEcB3mYVdXPMW1HO4zYzN4Gxb%2F%2FMB%2Fm5EOLgRmEINCXRmjJRYQYB3M74j%0ApwXS%0A)

\*\***Note**\*\*: Shared parameters cannot be edited directly from within individual test cases. You can only attach or detach them. All modifications must be made from the main Shared Parameters section.

## Deleting Shared Parameters

When deleting a shared parameter, you have two options:

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1657995096/0e53602807fd4ba7f07226fd27de/image.png?expires=1771427700&signature=75aff89bdcfeff3fa13e980df07467c1f925db3b4288edf03a4539f42bf736c5&req=dSYiEcB3mIFWX%2FMW1HO4zfKniGBsaiylWGJDyPGX1yreDcUq6fBlPndO11SG%0Ai%2B9DZDWjGc5g4%2FtT0AM%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1657995096/0e53602807fd4ba7f07226fd27de/image.png?expires=1771427700&signature=75aff89bdcfeff3fa13e980df07467c1f925db3b4288edf03a4539f42bf736c5&req=dSYiEcB3mIFWX%2FMW1HO4zfKniGBsaiylWGJDyPGX1yreDcUq6fBlPndO11SG%0Ai%2B9DZDWjGc5g4%2FtT0AM%3D%0A)

1. **Convert to Local Parameters**: Transform the shared parameter into individual local parameters within each test case.  
   ​
2. **Delete from All Test Cases**: Completely remove the parameter from all associated test cases.

## Tracking Usage of your shared parameter

You can view the usage of a shared parameter from the **Edit** screen by navigating to the **Usage** tab. This tab provides a detailed overview of:

* All projects that have access to the shared parameter.
* The number of test cases in the repository that use the shared parameter.
* The number of test cases submitted for review that include the shared parameter.

This allows you to quickly understand where and how your shared parameters are being utilized across your projects.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1682017577/1ed0e069de644a60efdcbdbed303/86794.png?expires=1771427700&signature=97bb57f071596c2c944e2198dee1397624dfd3871ca39a0b4661577fb8596578&req=dSYvFMl%2FmoRYXvMW1HO4zSBh4d7iS9vvdobrF0oEZ9Oq9XH4896aBZnS8FkG%0ABd4inKA3hWpnTZ0L4%2BE%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1682017577/1ed0e069de644a60efdcbdbed303/86794.png?expires=1771427700&signature=97bb57f071596c2c944e2198dee1397624dfd3871ca39a0b4661577fb8596578&req=dSYvFMl%2FmoRYXvMW1HO4zSBh4d7iS9vvdobrF0oEZ9Oq9XH4896aBZnS8FkG%0ABd4inKA3hWpnTZ0L4%2BE%3D%0A)

---

Related Articles

[Test Cases](https://help.qase.io/en/articles/5563704-test-cases)[Test Case Review](https://help.qase.io/en/articles/5563713-test-case-review)[How to write effective test cases?](https://help.qase.io/en/articles/8680192-how-to-write-effective-test-cases)[Ways to organize your test cases in a repository](https://help.qase.io/en/articles/8712163-ways-to-organize-your-test-cases-in-a-repository)[How to configure SSO with Okta](https://help.qase.io/en/articles/9889292-how-to-configure-sso-with-okta)