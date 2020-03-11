.PHONY: app.js clean clean-deps

app.js: 
	elm make --output build/app.js src/Main.elm

clean-deps:
	rm -rf elm-stuff

clean:
	rm -f build/*.js
	rm -rf elm-stuff/build-artifacts


default: app.js
