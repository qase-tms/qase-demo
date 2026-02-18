# Environments

Environments are an additional entity of Qase which allows you to represent your real-life infrastructure environments and then specify which of the environment a [Test Run](https://help.qase.io/en/articles/5563702-test-runs) should be executed in.

To create a new environment, navigate to the Project's "Environments" tab, then hit "Create new environment":

⚠️ Please note that only users with **the Owner** and **Administrator** roles, as well as, those with custom roles with create/update permissions, will have the access to create Environments.

[![](https://downloads.intercomcdn.com/i/o/1172393902/826104c314fd6ce4bafb4b48/image.png?expires=1771427700&signature=055367bf3be11546490fb14e188499d56dbe43ed018b06ba476d03196034f5b3&req=dSEgFMp3nohfW%2FMW1HO4zUjpWzfjJXE77i0%2FjhZJ7Z2z4untt7nHEh5wYHcq%0AZF0cQfQk8QP7%2Bsg3J7A%3D%0A)](https://downloads.intercomcdn.com/i/o/1172393902/826104c314fd6ce4bafb4b48/image.png?expires=1771427700&signature=055367bf3be11546490fb14e188499d56dbe43ed018b06ba476d03196034f5b3&req=dSEgFMp3nohfW%2FMW1HO4zUjpWzfjJXE77i0%2FjhZJ7Z2z4untt7nHEh5wYHcq%0AZF0cQfQk8QP7%2Bsg3J7A%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/1086340213/49206b265605e6a030e1dad6/image.png?expires=1771427700&signature=cac853b7109acc640cae7b867c63c9189cf8c9b96734d2c4f60a79851f38386f&req=dSAvEMp6nYNeWvMW1HO4zWsieoV6zA1RpoXsNR%2FwfNtP9Q9MwSMH%2FHWxOXVV%0A8rMYhiKR6o9nPgOiKYc%3D%0A)](https://downloads.intercomcdn.com/i/o/1086340213/49206b265605e6a030e1dad6/image.png?expires=1771427700&signature=cac853b7109acc640cae7b867c63c9189cf8c9b96734d2c4f60a79851f38386f&req=dSAvEMp6nYNeWvMW1HO4zWsieoV6zA1RpoXsNR%2FwfNtP9Q9MwSMH%2FHWxOXVV%0A8rMYhiKR6o9nPgOiKYc%3D%0A)

Define the new environment's properties:

* ***Title****:* mandatory field, descriptive name of an environment which will be appearing in the test runs (i.e., *Production Env*)
* ***Slug****:* mandatory field, a URL-friendly shortened version of the title (i.e., “*prod”*)
* *Description:* optional field for extra context about the environment and what it's to be used for
* *Host:* optional field, the URL address of the environment (as a reference)

Once created, your new environment can now be used as a property of a test run:

[![](https://downloads.intercomcdn.com/i/o/1086341209/11a78cc41ed53a1e93020ba1/image.png?expires=1771427700&signature=07d1b75a10168eb916f29d75c1e427eb263cc4019d15ff1297ef07faab3c8fa3&req=dSAvEMp6nINfUPMW1HO4za0KxOHcataYT3JKqwZDD%2FhO2KIVi%2F9Ja853qdvq%0AE5iRlKXM4VJqEBPLVBM%3D%0A)](https://downloads.intercomcdn.com/i/o/1086341209/11a78cc41ed53a1e93020ba1/image.png?expires=1771427700&signature=07d1b75a10168eb916f29d75c1e427eb263cc4019d15ff1297ef07faab3c8fa3&req=dSAvEMp6nINfUPMW1HO4za0KxOHcataYT3JKqwZDD%2FhO2KIVi%2F9Ja853qdvq%0AE5iRlKXM4VJqEBPLVBM%3D%0A)

When using the API, test runs can be created with a specific environment by using the environment's slug as a parameter in the request.

For example, when creating test runs with [`qli`](https://help.qase.io/en/articles/9789909-qase-cli-app), the `-e` flag can be used to define the environment for the new test run.

`qli testops run create -p DEMO -t <token> --title "Example Test run" -e prod`

Additionally, **`qli`** can also [create](https://help.qase.io/en/articles/9789909-qase-cli-app#h_6d74ecd478) an environment.

---

Related Articles

[Asana](https://help.qase.io/en/articles/6417211-asana)[GitHub](https://help.qase.io/en/articles/7210938-github)[GitLab](https://help.qase.io/en/articles/7210982-gitlab)[Qase CLI App](https://help.qase.io/en/articles/9789909-qase-cli-app)[AIDEN - AI Test Cloud](https://help.qase.io/en/articles/11851804-aiden-ai-test-cloud)