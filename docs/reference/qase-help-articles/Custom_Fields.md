# Custom Fields

***⚠️Custom Fields are available in [Startup](https://help.qase.io/en/articles/5563728-startup-plan), [Business](https://help.qase.io/en/articles/5563727-business-plan), and [Enterprise](https://help.qase.io/en/articles/6640055-enterprise-plan) subscriptions***

Obviously, test scenarios come with all varieties of data connected to them. It is pretty much impossible for us at Qase to predict every single data point you want to record for your [Test Cases](https://help.qase.io/en/articles/5563704-test-cases), [Test Runs](https://help.qase.io/en/articles/5563702-test-runs), or [Defects](https://help.qase.io/en/articles/5563710-defects).

So instead of trying to cover all bases or giving a bare minimum, we provide you with Custom Fields - a tool to create your own custom data entry points.

You'll need to create these Custom Fields first to be able to fill them in. To get started, navigate to the Workspace settings' "Fields" section:

[![](https://downloads.intercomcdn.com/i/o/1092404173/36e0b8ff5da5ea64d7c96d6c/image.png?expires=1771427700&signature=0440adc12d8d2e054b1e3e64b871dd267ea468f78c6abe2debfca4d848f3d9ed&req=dSAuFM1%2BmYBYWvMW1HO4zRVBAvb2HkPLhcwIosoYuauL81lOPHGQH3g51sQ0%0ADdjqnjL06SN1VelADK8%3D%0A)](https://downloads.intercomcdn.com/i/o/1092404173/36e0b8ff5da5ea64d7c96d6c/image.png?expires=1771427700&signature=0440adc12d8d2e054b1e3e64b871dd267ea468f78c6abe2debfca4d848f3d9ed&req=dSAuFM1%2BmYBYWvMW1HO4zRVBAvb2HkPLhcwIosoYuauL81lOPHGQH3g51sQ0%0ADdjqnjL06SN1VelADK8%3D%0A)

## Create a Custom Field

---

Create a new Custom Field by clicking "+ Create New Custom Field", configure your Custom Field, and define what it will be representing:

* *Title:* give a brief descriptive name to your Custom Field (Title is the only mandatory parameter).

[![](https://downloads.intercomcdn.com/i/o/1092404899/90b30481cf1fc89b2fe98bfe/image.png?expires=1771427700&signature=f150059938abc0a50066b0d90281de71edac14dc0caf76d49d6ff335a6cc92d1&req=dSAuFM1%2BmYlWUPMW1HO4zfmx0Vs88ZB6FX1mHnIdxx9o4O5Nd2xuYlKtxtI4%0A2Pd8Edba0YU3p4IbWp4%3D%0A)](https://downloads.intercomcdn.com/i/o/1092404899/90b30481cf1fc89b2fe98bfe/image.png?expires=1771427700&signature=f150059938abc0a50066b0d90281de71edac14dc0caf76d49d6ff335a6cc92d1&req=dSAuFM1%2BmYlWUPMW1HO4zfmx0Vs88ZB6FX1mHnIdxx9o4O5Nd2xuYlKtxtI4%0A2Pd8Edba0YU3p4IbWp4%3D%0A)

* *Entity:* define which Qase entities your Custom Field will apply to - Test Cases, Test Runs, or Defects. This parameter is a single-choice one, so you cannot select "Test Cases" AND "Test Runs"; if you need to track similar data for both Runs and Cases, you'll need to create two separate Custom Fields for that.

[![](https://downloads.intercomcdn.com/i/o/1092405647/527015f76b544c6e5e294959/image.png?expires=1771427700&signature=144e7995b189cc0c051eb386e023a35ed50e045b5009af7b68612613813076b7&req=dSAuFM1%2BmIdbXvMW1HO4zV75LfCUW165HkoNcZLJfYmzswQEC8XIWpnckr%2BB%0A9XuAK8JnvzeWaFE2cxA%3D%0A)](https://downloads.intercomcdn.com/i/o/1092405647/527015f76b544c6e5e294959/image.png?expires=1771427700&signature=144e7995b189cc0c051eb386e023a35ed50e045b5009af7b68612613813076b7&req=dSAuFM1%2BmIdbXvMW1HO4zV75LfCUW165HkoNcZLJfYmzswQEC8XIWpnckr%2BB%0A9XuAK8JnvzeWaFE2cxA%3D%0A)

* *Type:* select from a dropdown which data type will be used in this Custom Field. Depending on the type of data selected, the options below will be different.  
  ​***NB:*** *once a custom field has been created, its type cannot be changed.*

[![](https://downloads.intercomcdn.com/i/o/1092406676/a210a8d24b6e6c6d59ee1cb8/image.png?expires=1771427700&signature=00633cb2e34f6640aef8358ab0bcbe8574342b587b4136a17b23c249d8a56a47&req=dSAuFM1%2Bm4dYX%2FMW1HO4zRSQkZacRrD0dEIX2iUvs8sSi1tiJgatKwroRML2%0AYUD%2BXZljY9zdBGnpAqM%3D%0A)](https://downloads.intercomcdn.com/i/o/1092406676/a210a8d24b6e6c6d59ee1cb8/image.png?expires=1771427700&signature=00633cb2e34f6640aef8358ab0bcbe8574342b587b4136a17b23c249d8a56a47&req=dSAuFM1%2Bm4dYX%2FMW1HO4zRSQkZacRrD0dEIX2iUvs8sSi1tiJgatKwroRML2%0AYUD%2BXZljY9zdBGnpAqM%3D%0A)

* *Enable for all projects:* choose which Projects your custom field should be applied to. If you have to capture the same data uniformly in multiple projects, you don't have to create duplicates of a field for each project - create a custom field once and apply it to various projects:

[![](https://downloads.intercomcdn.com/i/o/1092409642/d6edfd043b6ad5ac9be3d9b3/image.png?expires=1771427700&signature=b62d809900a1912a06cb22626cc3fb5ef0354f63ce9dd0a19a0c7901f1fdbaa1&req=dSAuFM1%2BlIdbW%2FMW1HO4zcI1dU22hBzMo%2Bcqb7xOJGzVR3cV4Jpg%2BNtIelhj%0A49AAmI221uUozFnDF8U%3D%0A)](https://downloads.intercomcdn.com/i/o/1092409642/d6edfd043b6ad5ac9be3d9b3/image.png?expires=1771427700&signature=b62d809900a1912a06cb22626cc3fb5ef0354f63ce9dd0a19a0c7901f1fdbaa1&req=dSAuFM1%2BlIdbW%2FMW1HO4zcI1dU22hBzMo%2Bcqb7xOJGzVR3cV4Jpg%2BNtIelhj%0A49AAmI221uUozFnDF8U%3D%0A)

* *Placeholder:* provide a sample value that will appear in a field in a faded color, while the Custom Field remains empty. This can help avoid confusion about what should go into the field.

* *Default value:* to avoid having Custom Fields left blank, you can automatically insert a default value.

[![](https://downloads.intercomcdn.com/i/o/1092411001/49e4d153efdd2295113aa9ec/image.png?expires=1771427700&signature=0effbf7d0fcdcf6ff353e49486294338477c6ad56cfe90f624f148e78513ce98&req=dSAuFM1%2FnIFfWPMW1HO4zSQYLn8M6FDXMs2qJOKBtDQD%2BeUYqcaIofW5gGfB%0A2fPh1DMUA%2B9s2y3siTo%3D%0A)](https://downloads.intercomcdn.com/i/o/1092411001/49e4d153efdd2295113aa9ec/image.png?expires=1771427700&signature=0effbf7d0fcdcf6ff353e49486294338477c6ad56cfe90f624f148e78513ce98&req=dSAuFM1%2FnIFfWPMW1HO4zSQYLn8M6FDXMs2qJOKBtDQD%2BeUYqcaIofW5gGfB%0A2fPh1DMUA%2B9s2y3siTo%3D%0A)

* *Required field* checkbox: checking this box will make a field mandatory; an entity with such a Custom Field will not be created until the Custom Field is filled in.

[![](https://downloads.intercomcdn.com/i/o/1092411170/e601bd885b98ba7fa47545f9/image.png?expires=1771427700&signature=d86507ec028d466f211e2d667cfc1323d795760c7d48f06e58f231c2475b6490&req=dSAuFM1%2FnIBYWfMW1HO4zcQxbuxAr3t%2BttpUxmrCAVOg8Ky%2Bfiv8xJVQ0vog%0A3%2Bsj9rhqLjOpQEfwEUA%3D%0A)](https://downloads.intercomcdn.com/i/o/1092411170/e601bd885b98ba7fa47545f9/image.png?expires=1771427700&signature=d86507ec028d466f211e2d667cfc1323d795760c7d48f06e58f231c2475b6490&req=dSAuFM1%2FnIBYWfMW1HO4zcQxbuxAr3t%2BttpUxmrCAVOg8Ky%2Bfiv8xJVQ0vog%0A3%2Bsj9rhqLjOpQEfwEUA%3D%0A)

* *Values:* Available for Multiselect and Selectbox types of data, this area allows you to define values to choose from when filling out a custom field:

[![](https://downloads.intercomcdn.com/i/o/1092411630/50d554918fea27084c856d83/image.png?expires=1771427700&signature=13b4a37b8d68610c780e88aefdad3d2df1a7ef1eb528fc2ff23565d05a7a7490&req=dSAuFM1%2FnIdcWfMW1HO4zYkrzKT%2FuPSnk2xx%2Bn5teC2%2FKwOlGO2R1P6DqzSy%0A5DCvV69nwpAwFX23Tvg%3D%0A)](https://downloads.intercomcdn.com/i/o/1092411630/50d554918fea27084c856d83/image.png?expires=1771427700&signature=13b4a37b8d68610c780e88aefdad3d2df1a7ef1eb528fc2ff23565d05a7a7490&req=dSAuFM1%2FnIdcWfMW1HO4zYkrzKT%2FuPSnk2xx%2Bn5teC2%2FKwOlGO2R1P6DqzSy%0A5DCvV69nwpAwFX23Tvg%3D%0A)

Creating Values:

1. Click and hold the 6 dots to drag and drop your values when organizing their order.
2. Click the default "plus" icon to open the icon customization options.
3. You can choose from the default colors or input the Hex color code for the icon.
4. You can enter the icon code starting with "fas fa-" followed by the icon name chosen from the provided external link.
5. Add a new value input field
6. Delete a value input field

[![](https://downloads.intercomcdn.com/i/o/1092419182/5c8465df37ac78d455d6d466/image.png?expires=1771427700&signature=3da901863abb14a090339b020c0bf06628b86f6fa98e8d8e5b4e7acc72da2507&req=dSAuFM1%2FlIBXW%2FMW1HO4zbprlyYmG%2FSgNhCS8uJfw9suTjK1fdNJteOdBXH5%0AjOIg8A5s%2F4fo2vJlmRE%3D%0A)](https://downloads.intercomcdn.com/i/o/1092419182/5c8465df37ac78d455d6d466/image.png?expires=1771427700&signature=3da901863abb14a090339b020c0bf06628b86f6fa98e8d8e5b4e7acc72da2507&req=dSAuFM1%2FlIBXW%2FMW1HO4zbprlyYmG%2FSgNhCS8uJfw9suTjK1fdNJteOdBXH5%0AjOIg8A5s%2F4fo2vJlmRE%3D%0A)

When exporting into CSV, your Custom Fields will appear as new columns on the far right of your CSV file.  
​  
They will be named "cf\_1", "cf\_2", "cf\_3"... following the order of creation of your custom field in your Workspace Fields settings.  
​

[![](https://downloads.intercomcdn.com/i/o/1096106402/252d9cd43ac8933a8091e298/8a942290-4678-4e7b-abd5-47df34b7d8d3.png?expires=1771427700&signature=53c560b4651721fea7120591bd5e19e3a6a3236f888a42f66a02d6d0e7c54936&req=dSAuEMh%2Bm4VfW%2FMW1HO4zV2Hiy0PR7EbgWGNcqbypJADD6TBsntyMJRhP0JY%0AEClNcJSj%2FdC5eHEP2Yc%3D%0A)](https://downloads.intercomcdn.com/i/o/1096106402/252d9cd43ac8933a8091e298/8a942290-4678-4e7b-abd5-47df34b7d8d3.png?expires=1771427700&signature=53c560b4651721fea7120591bd5e19e3a6a3236f888a42f66a02d6d0e7c54936&req=dSAuEMh%2Bm4VfW%2FMW1HO4zV2Hiy0PR7EbgWGNcqbypJADD6TBsntyMJRhP0JY%0AEClNcJSj%2FdC5eHEP2Yc%3D%0A)

## Sort the Custom Fields

---

By default, custom fields are arranged in chronological order based on their creation time, meaning the most recently created field appears at the bottom of the list.

However, if you want certain fields to be displayed at the top for easier access, you can adjust their order.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1416110020/6f83c1d4aeed3a96469a30557b9c/57653.png?expires=1771427700&signature=4a2c0ccc3fd31483ab7322ff1b59fa911c2f8b7fa6e8baa40ebd8beb3cf9f19d&req=dSQmEMh%2FnYFdWfMW1HO4zVW93iFiwZqCrxvJe1I5RzkU7Nwm3ViTC6V48jVm%0AYE%2BruppKL8vP0Rmr6rw%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1416110020/6f83c1d4aeed3a96469a30557b9c/57653.png?expires=1771427700&signature=4a2c0ccc3fd31483ab7322ff1b59fa911c2f8b7fa6e8baa40ebd8beb3cf9f19d&req=dSQmEMh%2FnYFdWfMW1HO4zVW93iFiwZqCrxvJe1I5RzkU7Nwm3ViTC6V48jVm%0AYE%2BruppKL8vP0Rmr6rw%3D%0A)

To do this, go to **Workspace > Fields**, select any custom field, and update its **order value** to change its position.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1416108445/4f91d98fc80cb6e0ff4f3e7f7648/18592.png?expires=1771427700&signature=4e2c051b6298de2f91cc6ca127d7f8e7a88d4bb00e7d5ccce92ef6553c93cf56&req=dSQmEMh%2BlYVbXPMW1HO4zQpeH7myn9uQ4C1cx5kBVtIRb5nI7SmKX62B8gV%2F%0AaSkt4vz0tbcRYo9HQ%2BQ%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1416108445/4f91d98fc80cb6e0ff4f3e7f7648/18592.png?expires=1771427700&signature=4e2c051b6298de2f91cc6ca127d7f8e7a88d4bb00e7d5ccce92ef6553c93cf56&req=dSQmEMh%2BlYVbXPMW1HO4zQpeH7myn9uQ4C1cx5kBVtIRb5nI7SmKX62B8gV%2F%0AaSkt4vz0tbcRYo9HQ%2BQ%3D%0A)

You can also sort the list by the **order field** to view the updated arrangement.

[![](https://downloads.intercomcdn.com/i/o/wsaz8vex/1416114615/1dcf91237249e6dca4d77509aeb5/85978.png?expires=1771427700&signature=35a1ce3b56164f07198cda4cd471488e4a27c335a14ab7ea6d2ab5e534dee59f&req=dSQmEMh%2FmYdeXPMW1HO4zYNDQmXRossy%2BugYeALW3gHSU9YrT%2BiHn4OZ%2Flwm%0A4KqykEEr0Y3Lb0rdjg0%3D%0A)](https://downloads.intercomcdn.com/i/o/wsaz8vex/1416114615/1dcf91237249e6dca4d77509aeb5/85978.png?expires=1771427700&signature=35a1ce3b56164f07198cda4cd471488e4a27c335a14ab7ea6d2ab5e534dee59f&req=dSQmEMh%2FmYdeXPMW1HO4zYNDQmXRossy%2BugYeALW3gHSU9YrT%2BiHn4OZ%2Flwm%0A4KqykEEr0Y3Lb0rdjg0%3D%0A)

If you add the same order value to more than one field, those fields are ordered based on their creation time.

---

Related Articles

[Jira Cloud](https://help.qase.io/en/articles/6417207-jira-cloud)[Jira Server/Datacenter Plugin installation](https://help.qase.io/en/articles/6417212-jira-server-datacenter-plugin-installation)[GitLab](https://help.qase.io/en/articles/6640064-gitlab)[GitHub](https://help.qase.io/en/articles/7210938-github)[Working with the Qase CSV format](https://help.qase.io/en/articles/9855721-working-with-the-qase-csv-format)