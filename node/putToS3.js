const AWS = require('aws-sdk');
var s3 = new AWS.S3();
exports.handler = (event, context, callback) => {
    let encodedImage =JSON.parse(event.body).data;
    let decodedImage = Buffer.from(encodedImage, 'base64');
    var filePath = event.queryStringParameters.key
    var params = {
        "Body": decodedImage,
        "Bucket": "student-univ-avatar",
        "Key": filePath
    };
    s3.upload(params, function(err, data){
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