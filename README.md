# Physics-Tutoring-Portal

## Development

### Local Testing

1. Clone the repository
2. From within the server directory, run:
```
pip install -r requirements.txt
gunicorn app:app
```
3. Open http://localhost:[PORT]

### Submitting a PR

***Read This First***

Before merging into main, check with the rest of the team to make sure that deployment will not interfere with any demos/events that we might be holding. By default, we should aim for code freeze for ~2 hours before any major demo to allow ample time to revert changes if something goes wrong.

1. Create an issue / branch for dev work

    - All development work should be linked to an issue and should be performed in a branch from `dev`.     
    - Test all changes locally if possible (login will not work locally at the moment, so protected pages may be hard to test). 

2. Merge into `dev`

    - If time allows, get code reviewed before merging into `dev`. If not, summarize changes in the PR. 
    - When merging, squash multiple commits into a single merge commit unless there's a good reason not to. Merging into `dev` will automatically trigger a client-dev build. 
    - After merging, thoroughly test the production dev site. If everything looks good, feel free to make a PR to merge `dev` into `main`. 

3. Merge into `main`

    - Get code reviewed before merging into `main` if changes have been made since the last review, or if code was not reviewed before merging into dev.
    - If the merge includes commits from different issues, do not squash commits. If the changes from dev only include changes for one issue, squash commits before merging.
    - Mark issue(s) as closed/complete.
