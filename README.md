# FIFA-Tournament-Website

Website made for a small FIFA tournament to be hosted on a local area network

## Website Details

Django backend and Vue for the frontend compiled using webpack to be served by the Django server

## How to Run on Local Server

1. Find local ipv4 address
2. Change `base_url` to build at the same ipv4 address in `vue.config.js`
3. Run `npm run build`
4. Run `npm run serve`
5. Open a new terminal for the Django Server and run it using the ipv4 address `manage.py runserve [ipv4 address here]`

## Upgrade Ideas for next year

1. Undo result method
2. More interaction pages like the Poll
3. Mobile optimising
4. Host photos online for the player profiles
5. Shop page
