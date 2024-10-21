# AWS Secure CloudFront Origin Bucket (for CDK v2)

[![GitHub](https://img.shields.io/github/license/gammarers/aws-secure-cloudfront-origin-bucket?style=flat-square)](https://github.com/gammarers/aws-secure-cloudfront-origin-bucket/blob/main/LICENSE)
[![npm (scoped)](https://img.shields.io/npm/v/@gammarers/aws-secure-cloudfront-origin-bucket?style=flat-square)](https://www.npmjs.com/package/@gammarers/aws-secure-cloudfront-origin-bucket)
[![PyPI](https://img.shields.io/pypi/v/gammarers.aws-secure-cloudfront-origin-bucket?style=flat-square)](https://pypi.org/project/gammarers.aws-secure-cloudfront-origin-bucket/)
[![Nuget](https://img.shields.io/nuget/v/Gammarers.CDK.AWS.SecureCloudFrontOriginBucket?style=flat-square)](https://www.nuget.org/packages/Gammarers.CDK.AWS.ScureCloudFrontOriginBucket/)
[![GitHub Workflow Status (branch)](https://img.shields.io/github/actions/workflow/status/gammarers/aws-secure-cloudfront-origin-bucket/release.yml?branch=main&label=release&style=flat-square)](https://github.com/gammarers/aws-secure-cloudfront-origin-bucket/actions/workflows/release.yml)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/gammarers/aws-secure-cloudfront-origin-bucket?sort=semver&style=flat-square)](https://github.com/gammarers/aws-secure-cloudfront-origin-bucket/releases)

[![View on Construct Hub](https://constructs.dev/badge?package=@gammarers/aws-secure-cloudfront-origin-bucket)](https://constructs.dev/packages/@gammarers/aws-secure-cloudfront-origin-bucket)

An AWS CDK construct library to create secure S3 buckets for CloudFront origin.

## Install

### TypeScript

#### install by npm

```shell
npm install @gammarers/aws-secure-cloudfront-origin-bucket
```

#### install by yarn

```shell
yarn add @gammarers/aws-secure-cloudfront-origin-bucket
```

#### install by pnpm

```shell
pnpm add @gammarers/aws-secure-cloudfront-origin-bucket
```

#### install by bun

```shell
bun add @gammarers/aws-secure-cloudfront-origin-bucket
```

### Python

```shell
pip install gammarers.aws-secure-cloudfront-origin-bucket
```

### C# / .NET

```shell
dotnet add package gammarers.CDK.AWS.SecureCloudFrontOriginBucket
```

## Example

### for OAI(Origin Access Identity)

```python
import { SecureCloudFrontOriginBucket, SecureCloudFrontOriginType } from '@gammarers/aws-secure-cloudfront-origin-bucket';

const oai = new cloudfront.OriginAccessIdentity(stack, 'OriginAccessIdentity');

new SecureCloudFrontOriginBucket(stack, 'SecureCloudFrontOriginBucket', {
  bucketName: 'example-origin-bucket',
  cloudFrontOriginType: SecureCloudFrontOriginType.ORIGIN_ACCESS_IDENTITY,
  cloudFrontOriginAccessIdentityS3CanonicalUserId: oai.cloudFrontOriginAccessIdentityS3CanonicalUserId,
});
```

### for OAC(Origin Access Control)

```python
import { SecureCloudFrontOriginBucket, SecureCloudFrontOriginType } from '@gammarers/aws-secure-cloudfront-origin-bucket';

declare const distribution: cloudfront.Distribution;

new SecureCloudFrontOriginBucket(stack, 'SecureCloudFrontOriginBucket', {
  bucketName: 'example-origin-bucket',
  cloudFrontOriginType: SecureCloudFrontOriginType.ORIGIN_ACCESS_CONTROL,
  cloudFrontArn: `arn:aws:cloudfront::123456789:distribution/${distribution.distributionId}`,
});
```

## License

This project is licensed under the Apache-2.0 License.
