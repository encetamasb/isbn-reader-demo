CUR_UID = $(shell id -u)
CUR_GID = $(shell id -g)

.PHONY: app.js clean clean-deps env

app.js: 
	elm make --output build/app.js src/Main.elm

clean-deps:
	rm -rf elm-stuff

clean:
	rm -f build/*.js
	rm -rf elm-stuff/build-artifacts

env:
	printf '%s\n%s\n' "UID=${CUR_UID}" "GID=${CUR_GID}" > .env

default: app.js
