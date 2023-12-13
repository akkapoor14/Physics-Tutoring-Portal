# Physics-Tutoring-Portal

## Project Overview
In a four-person team, designed, created, and deployed a three-tier web app to match Princeton physics students with tutors, creating a portal for each user type: student, tutor, and admin. Used GitHub for effective collaborative development. Hosted the frontend and backend servers on Render and ran both servers using the Python Flask Framework. Coded the frontend using HTML with the Jinja2 Template Engine and styling languages and frameworks such as CSS, SASS, and Bootstrap. For the backend, used Flask to expose our API to the frontend in combination with Marshmallow for simple parameter validation, and Flask-SQLAlchemy as our ORM for sending queries to our database and for defining datamodels. Used PostgreSQL as our database management system, and hosted our database remotely through bit.io. Implemented Princeton University’s CAS system for user authentication. Created a programmer’s guide, users’ guide, and product evaluation including detailed descriptions and diagrams of all use cases, all three layers of the tech stack, and all our app testing. Presented app with a demonstration and pitch to instructors and classmates.

Project Overview: https://drive.google.com/file/d/1vSvA_hnoBAPq6eCj3wvh_DLugw1gTBsY/view?usp=sharing

Programmer's Guide: https://drive.google.com/file/d/1Zrj9IVHvryTTL0qNYx8cvYrsXU7CnRze/view?usp=sharing

User's Guide: https://drive.google.com/file/d/1VDOAqmgd-ES0AHTcgIgNwRfgOVS-Xo7G/view?usp=sharing 

Product Eval: https://drive.google.com/file/d/1XUndY2_W98letPpol14IRAtLC8YbyOlm/view?usp=sharing

Project Eval: https://drive.google.com/file/d/10-4MJKyQDZEKPSut65St8eR_d4f7lmMl/view?usp=sharing

## Development

### Setup

There is more information in the `README.md` files in both `client` and `dev` directories.

1. Clone the repository.
2. Install all packages with `$ pip install -r requirements.txt`.
3. Install and run [Postgres](https://www.postgresql.org/download/).
4. Get any `.env` files from a team member.
5. In client and/or server directories run `$ flask run`.

### Submitting a PR

***Read This First***

Before merging into main, check with the rest of the team to make sure that deployment will not interfere with any demos/events that we might be holding. By default, we should aim for code freeze for ~2 hours before any major demo to allow ample time to revert changes if something goes wrong.

1. Create an issue / branch for dev work

    - All development work should be linked to an issue and should be performed in a branch from `dev`.     
    - Test all changes locally if possible (login will not work locally at the moment, so protected pages may be hard to test).
    - When committing, you must use the [scemantic commit message](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) convetions.

2. Merge into `dev`

    - When you merge any work into the `dev` branch, it will automatically trigger a new deploy. `dev` should only be used for testing polished work.
    - If time allows, get code reviewed before merging into `dev`. If not, summarize changes in the PR. 
    - When merging, *squash multiple commits* into a single merge commit unless there's a good reason not to. Merging into `dev` will automatically trigger a client-dev build. 
    - After merging, thoroughly test the dev site. If everything looks good, feel free to make a PR to merge `dev` into `main`. 

3. Merge into `main`

    - When you merge any work into the `main` branch, it will automatically trigger a new deploy.
    - Get code reviewed before merging into `main` if changes have been made since the last review, or if code was not reviewed before merging into dev.
    - If the merge includes commits from different issues, do not squash commits. If the changes from dev only include changes for one issue, squash commits before merging.
    - Mark issue(s) as closed/complete.
