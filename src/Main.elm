module Main exposing (main)

import Browser
import Html exposing (Html, div, text)


type Msg
    = NoOp


type alias Model =
    {}


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    ( model, Cmd.none )


view : Model -> Html Msg
view model =
    div [] [ text "This is a beginning of a beaut..." ]


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none


init : () -> ( Model, Cmd Msg )
init flags =
    ( {}, Cmd.none )


main =
    Browser.element
        { init = init
        , update = update
        , view = view
        , subscriptions = subscriptions
        }
