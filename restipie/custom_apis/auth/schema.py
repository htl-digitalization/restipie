signup_schema = {
	"$schema":"http://json-schema.org/draft-07/schema#",
	"title":"Sign up",
	"type" : "object",
	"properties" : {
		"fullname" : {
			"type" : "string",
			"minLength": 2,
			"maxLength": 64
		},
		"mobile_no": { "type" : "string", "pattern": "^[0-9]{11}$" },
		"email": { "type" : "string", "format": "email" },
		"location": {
			"type" : "string",
			"minLength": 5,
			"maxLength": 150
		}
	},
	"required": ["fullname", "mobile_no", "email"]
}


simple_login_schema = {
	"$schema":"http://json-schema.org/draft-07/schema#",
	"title":"Login",
	"type" : "object",
	"properties" : {
		"email": { "type": "string", "format": "email" },
		"password": { "type": "string" },
	},
	"required": ["email", "password"],

}


login_schema = {
	"$schema":"http://json-schema.org/draft-07/schema#",
	"title":"Login",
	"type" : "object",
	"properties" : {
		"login_by" : {
			"enum": ["email", "mobile_no"]
		}
	},
	"required": ["fullname", "mobile_no", "email"],
	"if": {
		"properties": { "login_by": { "const": "email" } }
	},
	"then": {
		"properties": {
			"email": { "type": "string", "format": "email" },
			"password": { "type": "string", "format": "email" }
		}
	},
	"else": {
		"properties": { "mobile_no": { "type" : "string", "pattern": "^[0-9]{11}$" } }
	}
}
