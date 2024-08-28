# astro_template
Test of the propagation changes to depended repositories.

All changes made to the main branch of this repository should be mirrored in the dependent repositories.
Dependent repositories are defined by the pattern "astro-".

After the commit of the PR to the main branch of the base repository,the PRs should be created in the dependent repositories for dev and main branches.

Possible scenarios:
1. Ideal option 🚀 The PR was merged into the main branch of the **base repository** 

        🛠️ The PRs had been created in dependent projects automatically

        ✅ Was manually merged into branches in those dependent projects

2. Ideal option 🚀 The PR was merged into the main branch of the **base repository**

        🛠️ The PRs had been created in dependent projects automatically 
   
        ❌ The PRs weren't merged in those dependent projects
   
   🚀 The new PR was merged into the main branch of the **base repository**

        🛠️ The PRs had been updated in dependent projects automatically

        ✅ was manually merged into branches in those dependent projects.

3. Conflict option 🚀 The PR was merged into the main branch of the **base repository**

        🛠️ The PRs had been created in dependent projects automatically

        ❌ The PRs weren't merged in those dependent projects

        📝 In existing PRs were added changes and weren't merged in dependent projects.

   🚀 The new PR was merged into the main branch of the **base repository**

        🛠️ The PRs had been updated in dependent projects in force-pushed mode and overwrite the changes❓ automatically 

        ✅ was manually merged into branches in those dependent projects.
