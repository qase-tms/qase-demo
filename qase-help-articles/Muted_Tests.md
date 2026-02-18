# Muted Tests

Test cases in Qase can be marked **muted**. This functionality is especially useful for handling flaky tests or those test cases that are currently less critical. When a test is marked as "muted", its results will not affect the overall status of test runs.

This means your test runs can still pass even if a muted test fails, preventing unnecessary delays in your release process.

## How to mark a test case "muted":

---

**👉 Ability to mute or unmute test cases is regulated by a user permission "Mute/Unmute" in the "Test cases" category of a [user role](https://help.qase.io/en/articles/5563741-workspace-management-roles-permissions).**

**Among the system roles, it is enabled for Owner and Administrator roles.  
For custom user roles, it can be granted through editing a custom role.**

1. In the repository, open a test case in the preview sidebar, switch to the "Properties" tab and check the box for "Muted case":  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1025625423/dc4578dcb487be56245199e9/image.png?expires=1771427700&signature=6b5af3ce071cd0e1a2512ccae12223c8690136bcde7dbd82bddc17f0feb09452&req=dSAlE898mIVdWvMW1HO4zbjBivzLKdG6ufoVi50ADquS0hjpH%2FqVblqvMK5b%0A0swr%0A)](https://downloads.intercomcdn.com/i/o/1025625423/dc4578dcb487be56245199e9/image.png?expires=1771427700&signature=6b5af3ce071cd0e1a2512ccae12223c8690136bcde7dbd82bddc17f0feb09452&req=dSAlE898mIVdWvMW1HO4zbjBivzLKdG6ufoVi50ADquS0hjpH%2FqVblqvMK5b%0A0swr%0A)
2. Open a test case in edition mode, and check the box for "Muted case":  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1025626983/4f18474d1012fcbff3252599/image.png?expires=1771427700&signature=01922280e2491dff911ea5931ce8e859c3808dd9d9cbb1fc8289f8980f076c36&req=dSAlE898m4hXWvMW1HO4zak0kWiSGfDmhjupXdKLrvbm3HgChJ85tYCeuE8O%0A6cYE%0A)](https://downloads.intercomcdn.com/i/o/1025626983/4f18474d1012fcbff3252599/image.png?expires=1771427700&signature=01922280e2491dff911ea5931ce8e859c3808dd9d9cbb1fc8289f8980f076c36&req=dSAlE898m4hXWvMW1HO4zak0kWiSGfDmhjupXdKLrvbm3HgChJ85tYCeuE8O%0A6cYE%0A)
3. Select multiple cases in the repository and bulk edit them, checking the "Muted" box:  
   ​

   [![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304820606/03ea4f49cc242e1bca404e25c182/95036.png?expires=1771427700&signature=d32d9c9b860736be9a37f004f6b2bb01cdadb8ee0bb5ae84bfc7391f32c0c81e&req=dSMnEsF8nYdfX%2FMW1HO4zVavx4%2Boo%2B2smpCHSA%2B%2FphjJmDmzX0eh2gS9%2BblQ%0AH9Di%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1304820606/03ea4f49cc242e1bca404e25c182/95036.png?expires=1771427700&signature=d32d9c9b860736be9a37f004f6b2bb01cdadb8ee0bb5ae84bfc7391f32c0c81e&req=dSMnEsF8nYdfX%2FMW1HO4zVavx4%2Boo%2B2smpCHSA%2B%2FphjJmDmzX0eh2gS9%2BblQ%0AH9Di%0A)

   ​

   [![](https://downloads.intercomcdn.com/i/o/1025630912/d23ba8716a256669815225bb/image.png?expires=1771427700&signature=8c04bfd19ffaf795911267db34c227062cc8f5b0a64edc5d7001015fe4e28f98&req=dSAlE899nYheW%2FMW1HO4zfG%2BbZlrmrN6g%2BafhcLfgAmszHO3vu4rI8teRpFt%0AIY0q%0A)](https://downloads.intercomcdn.com/i/o/1025630912/d23ba8716a256669815225bb/image.png?expires=1771427700&signature=8c04bfd19ffaf795911267db34c227062cc8f5b0a64edc5d7001015fe4e28f98&req=dSAlE899nYheW%2FMW1HO4zfG%2BbZlrmrN6g%2BafhcLfgAmszHO3vu4rI8teRpFt%0AIY0q%0A)
4. In a test run, select a test case and click the "Mute" button above the result statuses:  
   ​

   [![](https://downloads.intercomcdn.com/i/o/1025632890/0b4dc746340eb8c90e2eee92/image.png?expires=1771427700&signature=7dc51c04d39826d04f2c2d8a932d65e87610bf6f785b48382fb567b8e9fc575b&req=dSAlE899n4lWWfMW1HO4zR7crUM%2BrSciRC5VcdgyV1QYmYku%2FAnBe7QRxEEh%0ASGfB%0A)](https://downloads.intercomcdn.com/i/o/1025632890/0b4dc746340eb8c90e2eee92/image.png?expires=1771427700&signature=7dc51c04d39826d04f2c2d8a932d65e87610bf6f785b48382fb567b8e9fc575b&req=dSAlE899n4lWWfMW1HO4zR7crUM%2BrSciRC5VcdgyV1QYmYku%2FAnBe7QRxEEh%0ASGfB%0A)

## Recognising Muted test cases:

---

### In the repository:

[![](https://downloads.intercomcdn.com/i/o/1025638600/f7d825bcb674c0eea5d91cbd/image.png?expires=1771427700&signature=a5b98f9fcf023225cd8e78acbb36b27fda8494cf07c28960d60ecaaa4c106072&req=dSAlE899lYdfWfMW1HO4zZuAIzMiM9mUa%2Bx%2B9DPZIGFCJyPkPdF1P60ssKBM%0AbQPzn4lRFqWzweLuskw%3D%0A)](https://downloads.intercomcdn.com/i/o/1025638600/f7d825bcb674c0eea5d91cbd/image.png?expires=1771427700&signature=a5b98f9fcf023225cd8e78acbb36b27fda8494cf07c28960d60ecaaa4c106072&req=dSAlE899lYdfWfMW1HO4zZuAIzMiM9mUa%2Bx%2B9DPZIGFCJyPkPdF1P60ssKBM%0AbQPzn4lRFqWzweLuskw%3D%0A)

### In the Test runs:

[![](https://downloads.intercomcdn.com/i/o/1025639153/adc00983d0e29b1e0424ba91/image.png?expires=1771427700&signature=f02d6fbc6f61dac40dab75ae6cbef0543f0720c84547073935c366115f5767cf&req=dSAlE899lIBaWvMW1HO4zdNKgneSo7Mu%2Fs90XOnhZqzfDULHu1RhsSGmmgAu%0AW6Yxv1MQkz14OeO34IU%3D%0A)](https://downloads.intercomcdn.com/i/o/1025639153/adc00983d0e29b1e0424ba91/image.png?expires=1771427700&signature=f02d6fbc6f61dac40dab75ae6cbef0543f0720c84547073935c366115f5767cf&req=dSAlE899lIBaWvMW1HO4zdNKgneSo7Mu%2Fs90XOnhZqzfDULHu1RhsSGmmgAu%0AW6Yxv1MQkz14OeO34IU%3D%0A)

**If a test case has been "muted" from a test run, it will also appear "muted" in the repository.**

Any previously muted test case can be "unmuted" at any time by unchecking the "Muted case" box when editing a test case - or by clicking an "Unmute" button when viewing the test case in a test run:

[![](https://downloads.intercomcdn.com/i/o/1025642419/d938c0768e7aa8f0258f3ff6/image.png?expires=1771427700&signature=dce7d02d28259b867ce51fdc57926dc555cbac3a0e6112aec6cf472cd8a22425&req=dSAlE896n4VeUPMW1HO4za1C2seKg%2BIJ45bofr6aCkvWE0SKUlcRIoVuwjpw%0AasPlZSoq829fLQbomfk%3D%0A)](https://downloads.intercomcdn.com/i/o/1025642419/d938c0768e7aa8f0258f3ff6/image.png?expires=1771427700&signature=dce7d02d28259b867ce51fdc57926dc555cbac3a0e6112aec6cf472cd8a22425&req=dSAlE896n4VeUPMW1HO4za1C2seKg%2BIJ45bofr6aCkvWE0SKUlcRIoVuwjpw%0AasPlZSoq829fLQbomfk%3D%0A)

## What does Muting a test do?

---

* If a test run includes a muted test case, then a Failed, Invalid, Blocked result (or a custom result of a "Failure" type) submitted for such a case will not affect the completion status of the test run, i.e. having failed a muted test case will not result in the test run getting marked failed:  
  ​

  [![](https://downloads.intercomcdn.com/i/o/1025649110/32ce2844b6c67eb6ee359c11/image.png?expires=1771427700&signature=7dd363fa7dc12554f5fb02c95d31fb3637adfa403b0e23becdd0300ac929a28a&req=dSAlE896lIBeWfMW1HO4zVQG8kM6CBrLBS%2B5qtYpFrECJs4nQF48eClkU6HT%0AbEas%0A)](https://downloads.intercomcdn.com/i/o/1025649110/32ce2844b6c67eb6ee359c11/image.png?expires=1771427700&signature=7dd363fa7dc12554f5fb02c95d31fb3637adfa403b0e23becdd0300ac929a28a&req=dSAlE896lIBeWfMW1HO4zVQG8kM6CBrLBS%2B5qtYpFrECJs4nQF48eClkU6HT%0AbEas%0A)
* ❗ If a test run already has a completion status (Passed/Failed), even after extra test cases were added into it or cases were muted - after the run was completed - the completion status of the run will not be recalculated;
* When [parametrized test cases](https://help.qase.io/en/articles/6640037-test-case-parameters) are included in a run, marking one of the parametrized siblings "muted" will also mute all the other parametrized versions of such a test case.

---

Related Articles

[Getting Started](https://help.qase.io/en/articles/5563688-getting-started)[Test Runs](https://help.qase.io/en/articles/5563702-test-runs)[Test Cases](https://help.qase.io/en/articles/5563704-test-cases)[GitHub](https://help.qase.io/en/articles/7210938-github)[AIDEN - AI Test Cloud](https://help.qase.io/en/articles/11851804-aiden-ai-test-cloud)