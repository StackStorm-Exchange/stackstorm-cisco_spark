# Cisco Spark Integration Pack

This integration pack allows you to integrate with
[Cisco Spark](http://www.ciscospark.com/),
the Enterprise Voice, instant messaging and collaboration platform by Cisco.

## Using the Webhook

You can use `hubot-spark` with Cisco Spark configuration. This can also
be combined with webhooks by enabling the ChatOps rule.

## Actions

Currently, the following actions listed below are supported:

### Message actions

* `send_message`
* `get_message`
* `list_messages`
* `delete_message`

### Room actions

* `create_room`
* `get_room`
* `update_room`
* `list_rooms`
* `delete_room`

### Team actions

* `create_team`
* `get_team`
* `update_team`
* `list_teams`
* `delete_team`

### Webhook actions

* `create_webhook`
* `get_webhook`
* `update_webhook`
* `list_webhooks`
* `delete_webhook`

## Configuration

Copy the example configuration in [cisco_spark.yaml.example](./cisco_spark.yaml.example)
to `/opt/stackstorm/configs/cisco_spark.yaml` and edit as required.

It must contain:

* `access_token` - The API access token, can be fetched from developer.ciscospark.com

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`
