const AWS = require('aws-sdk');
var s3 = new AWS.S3();
exports.handler = (event, context, callback) => {
    var params = {
        "Bucket": "student-univ-avatar",
        "Key": event.queryStringParameters.key
    };
    s3.getObject(params, function(err, data){
        if(err) {
            callback(err, null);
        } else {
            let response = {
                "statusCode": 200,
                "body": JSON.stringify(data),
                "isBase64Encoded": false,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Credentials": "true"
                }
            };
            callback(null, response);
        }
    });
};