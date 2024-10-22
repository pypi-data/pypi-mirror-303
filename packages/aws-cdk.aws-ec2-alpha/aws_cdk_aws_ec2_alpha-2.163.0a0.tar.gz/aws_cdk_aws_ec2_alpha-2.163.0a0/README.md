# Amazon VpcV2 Construct Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

## VpcV2

`VpcV2` is a re-write of the [`ec2.Vpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Vpc.html) construct. This new construct enables higher level of customization
on the VPC being created. `VpcV2` implements the existing [`IVpc`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html), therefore,
`VpcV2` is compatible with other constructs that accepts `IVpc` (e.g. [`ApplicationLoadBalancer`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticloadbalancingv2.ApplicationLoadBalancer.html#construct-props)).

To create a VPC with both IPv4 and IPv6 support:

```python
stack = Stack()
VpcV2(self, "Vpc",
    primary_address_block=IpAddresses.ipv4("10.0.0.0/24"),
    secondary_address_blocks=[
        IpAddresses.amazon_provided_ipv6(cidr_block_name="AmazonProvidedIpv6")
    ]
)
```

`VpcV2` does not automatically create subnets or allocate IP addresses, which is different from the `Vpc` construct.

Importing existing VPC in an account into CDK as a `VpcV2` is not yet supported.

## SubnetV2

`SubnetV2` is a re-write of the [`ec2.Subnet`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.Subnet.html) construct.
This new construct can be used to add subnets to a `VpcV2` instance:

```python
stack = Stack()
my_vpc = VpcV2(self, "Vpc",
    secondary_address_blocks=[
        IpAddresses.amazon_provided_ipv6(cidr_block_name="AmazonProvidedIp")
    ]
)

SubnetV2(self, "subnetA",
    vpc=my_vpc,
    availability_zone="us-east-1a",
    ipv4_cidr_block=IpCidr("10.0.0.0/24"),
    ipv6_cidr_block=IpCidr("2a05:d02c:25:4000::/60"),
    subnet_type=SubnetType.PRIVATE_ISOLATED
)
```

Same as `VpcV2`, importing existing subnets is not yet supported.

## IP Addresses Management

By default `VpcV2` uses `10.0.0.0/16` as the primary CIDR if none is defined.
Additional CIDRs can be adding to the VPC via the `secondaryAddressBlocks` prop.
The following example illustrates the different options of defining the address blocks:

```python
stack = Stack()
ipam = Ipam(self, "Ipam",
    operating_region=["us-west-1"]
)
ipam_public_pool = ipam.public_scope.add_pool("PublicPoolA",
    address_family=AddressFamily.IP_V6,
    aws_service=AwsServiceName.EC2,
    locale="us-west-1",
    public_ip_source=IpamPoolPublicIpSource.AMAZON
)
ipam_public_pool.provision_cidr("PublicPoolACidrA", netmask_length=52)

ipam_private_pool = ipam.private_scope.add_pool("PrivatePoolA",
    address_family=AddressFamily.IP_V4
)
ipam_private_pool.provision_cidr("PrivatePoolACidrA", netmask_length=8)

VpcV2(self, "Vpc",
    primary_address_block=IpAddresses.ipv4("10.0.0.0/24"),
    secondary_address_blocks=[
        IpAddresses.amazon_provided_ipv6(cidr_block_name="AmazonIpv6"),
        IpAddresses.ipv6_ipam(
            ipam_pool=ipam_public_pool,
            netmask_length=52,
            cidr_block_name="ipv6Ipam"
        ),
        IpAddresses.ipv4_ipam(
            ipam_pool=ipam_private_pool,
            netmask_length=8,
            cidr_block_name="ipv4Ipam"
        )
    ]
)
```

Since `VpcV2` does not create subnets automatically, users have full control over IP addresses allocation across subnets.

## Routing

`RouteTable` is a new construct that allows for route tables to be customized in a variety of ways. For instance, the following example shows how a custom route table can be created and appended to a subnet:

```python
my_vpc = VpcV2(self, "Vpc")
route_table = RouteTable(self, "RouteTable",
    vpc=my_vpc
)
subnet = SubnetV2(self, "Subnet",
    vpc=my_vpc,
    route_table=route_table,
    availability_zone="eu-west-2a",
    ipv4_cidr_block=IpCidr("10.0.0.0/24"),
    subnet_type=SubnetType.PRIVATE_ISOLATED
)
```

`Routes` can be created to link subnets to various different AWS services via gateways and endpoints. Each unique route target has its own dedicated construct that can be routed to a given subnet via the `Route` construct. An example using the `InternetGateway` construct can be seen below:

```python
stack = Stack()
my_vpc = VpcV2(self, "Vpc")
route_table = RouteTable(self, "RouteTable",
    vpc=my_vpc
)
subnet = SubnetV2(self, "Subnet",
    vpc=my_vpc,
    availability_zone="eu-west-2a",
    ipv4_cidr_block=IpCidr("10.0.0.0/24"),
    subnet_type=SubnetType.PRIVATE_ISOLATED
)

igw = InternetGateway(self, "IGW",
    vpc=my_vpc
)
Route(self, "IgwRoute",
    route_table=route_table,
    destination="0.0.0.0/0",
    target={"gateway": igw}
)
```

Alternatively, `Routes` can also be created via method `addRoute` in the `RouteTable` class. An example using the `EgressOnlyInternetGateway` construct can be seen below:
Note: `EgressOnlyInternetGateway` can only be used to set up outbound IPv6 routing.

```python
stack = Stack()
my_vpc = VpcV2(self, "Vpc",
    primary_address_block=IpAddresses.ipv4("10.1.0.0/16"),
    secondary_address_blocks=[IpAddresses.amazon_provided_ipv6(
        cidr_block_name="AmazonProvided"
    )]
)

eigw = EgressOnlyInternetGateway(self, "EIGW",
    vpc=my_vpc
)

route_table = RouteTable(self, "RouteTable",
    vpc=my_vpc
)

route_table.add_route("EIGW", "::/0", {"gateway": eigw})
```

Other route targets may require a deeper set of parameters to set up properly. For instance, the example below illustrates how to set up a `NatGateway`:

```python
my_vpc = VpcV2(self, "Vpc")
route_table = RouteTable(self, "RouteTable",
    vpc=my_vpc
)
subnet = SubnetV2(self, "Subnet",
    vpc=my_vpc,
    availability_zone="eu-west-2a",
    ipv4_cidr_block=IpCidr("10.0.0.0/24"),
    subnet_type=SubnetType.PRIVATE_ISOLATED
)

natgw = NatGateway(self, "NatGW",
    subnet=subnet,
    vpc=my_vpc,
    connectivity_type=NatConnectivityType.PRIVATE,
    private_ip_address="10.0.0.42"
)
Route(self, "NatGwRoute",
    route_table=route_table,
    destination="0.0.0.0/0",
    target={"gateway": natgw}
)
```

It is also possible to set up endpoints connecting other AWS services. For instance, the example below illustrates the linking of a Dynamo DB endpoint via the existing `ec2.GatewayVpcEndpoint` construct as a route target:

```python
stack = Stack()
my_vpc = VpcV2(self, "Vpc")
route_table = RouteTable(self, "RouteTable",
    vpc=my_vpc
)
subnet = SubnetV2(self, "Subnet",
    vpc=my_vpc,
    availability_zone="eu-west-2a",
    ipv4_cidr_block=IpCidr("10.0.0.0/24"),
    subnet_type=SubnetType.PRIVATE
)

dynamo_endpoint = ec2.GatewayVpcEndpoint(self, "DynamoEndpoint",
    service=ec2.GatewayVpcEndpointAwsService.DYNAMODB,
    vpc=my_vpc,
    subnets=[subnet]
)
Route(self, "DynamoDBRoute",
    route_table=route_table,
    destination="0.0.0.0/0",
    target={"endpoint": dynamo_endpoint}
)
```

## Adding Egress-Only Internet Gateway to VPC

An egress-only internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows outbound communication over IPv6 from instances in your VPC to the internet, and prevents the internet from initiating an IPv6 connection with your instances.

For more information see [Enable outbound IPv6 traffic using an egress-only internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html).

VpcV2 supports adding an egress only internet gateway to VPC using the `addEgressOnlyInternetGateway` method.

By default, this method sets up a route to all outbound IPv6 address ranges, unless a specific destination is provided by the user. It can only be configured for IPv6-enabled VPCs.
The `Subnets` parameter accepts a `SubnetFilter`, which can be based on a `SubnetType` in VpcV2. A new route will be added to the route tables of all subnets that match this filter.

```python
stack = Stack()
my_vpc = VpcV2(self, "Vpc",
    primary_address_block=IpAddresses.ipv4("10.1.0.0/16"),
    secondary_address_blocks=[IpAddresses.amazon_provided_ipv6(
        cidr_block_name="AmazonProvided"
    )]
)
route_table = RouteTable(self, "RouteTable",
    vpc=my_vpc
)
subnet = SubnetV2(self, "Subnet",
    vpc=my_vpc,
    availability_zone="eu-west-2a",
    ipv4_cidr_block=IpCidr("10.0.0.0/24"),
    ipv6_cidr_block=IpCidr("2001:db8:1::/64"),
    subnet_type=SubnetType.PRIVATE
)

my_vpc.add_egress_only_internet_gateway(
    subnets=[ec2.SubnetSelection(subnet_type=SubnetType.PRIVATE)],
    destination="::/60"
)
```

## Adding NATGateway to the VPC

A NAT gateway is a Network Address Translation (NAT) service.You can use a NAT gateway so that instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.

For more information, see [NAT gateway basics](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html).

When you create a NAT gateway, you specify one of the following connectivity types:

**Public – (Default)**: Instances in private subnets can connect to the internet through a public NAT gateway, but cannot receive unsolicited inbound connections from the internet

**Private**: Instances in private subnets can connect to other VPCs or your on-premises network through a private NAT gateway.

To define the NAT gateway connectivity type as `ConnectivityType.Public`, you need to ensure that there is an IGW(Internet Gateway) attached to the subnet's VPC.
Since a NATGW is associated with a particular subnet, providing `subnet` field in the input props is mandatory.

Additionally, you can set up a route in any route table with the target set to the NAT Gateway. The function `addNatGateway` returns a `NATGateway` object that you can reference later.

The code example below provides the definition for adding a NAT gateway to your subnet:

```python
stack = Stack()
my_vpc = VpcV2(self, "Vpc")
route_table = RouteTable(self, "RouteTable",
    vpc=my_vpc
)
subnet = SubnetV2(self, "Subnet",
    vpc=my_vpc,
    availability_zone="eu-west-2a",
    ipv4_cidr_block=IpCidr("10.0.0.0/24"),
    subnet_type=SubnetType.PUBLIC
)

my_vpc.add_internet_gateway()
my_vpc.add_nat_gateway(
    subnet=subnet,
    connectivity_type=NatConnectivityType.PUBLIC
)
```

## Enable VPNGateway for the VPC

A virtual private gateway is the endpoint on the VPC side of your VPN connection.

For more information, see [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html).

VPN route propagation is a feature in Amazon Web Services (AWS) that automatically updates route tables in your Virtual Private Cloud (VPC) with routes learned from a VPN connection.

To enable VPN route propogation, use the `vpnRoutePropagation` property to specify the subnets as an input to the function. VPN route propagation will then be enabled for each subnet with the corresponding route table IDs.

Additionally, you can set up a route in any route table with the target set to the VPN Gateway. The function `enableVpnGatewayV2` returns a `VPNGatewayV2` object that you can reference later.

The code example below provides the definition for setting up a VPN gateway with `vpnRoutePropogation` enabled:

```python
stack = Stack()
my_vpc = VpcV2(self, "Vpc")
vpn_gateway = my_vpc.enable_vpn_gateway_v2(
    vpn_route_propagation=[ec2.SubnetSelection(subnet_type=SubnetType.PUBLIC)],
    type=VpnConnectionType.IPSEC_1
)

route_table = RouteTable(stack, "routeTable",
    vpc=my_vpc
)

Route(stack, "route",
    destination="172.31.0.0/24",
    target={"gateway": vpn_gateway},
    route_table=route_table
)
```

## Adding InternetGateway to the VPC

An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. It supports both IPv4 and IPv6 traffic.

For more information, see [Enable VPC internet access using internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-igw-internet-access.html).

You can add an internet gateway to a VPC using `addInternetGateway` method. By default, this method creates a route in all Public Subnets with outbound destination set to `0.0.0.0` for IPv4 and `::0` for IPv6 enabled VPC.
Instead of using the default settings, you can configure a custom destinatation range by providing an optional input `destination` to the method.

The code example below shows how to add an internet gateway with a custom outbound destination IP range:

```python
stack = Stack()
my_vpc = VpcV2(self, "Vpc")

subnet = SubnetV2(self, "Subnet",
    vpc=my_vpc,
    availability_zone="eu-west-2a",
    ipv4_cidr_block=IpCidr("10.0.0.0/24"),
    subnet_type=SubnetType.PUBLIC
)

my_vpc.add_internet_gateway(
    ipv4_destination="192.168.0.0/16"
)
```
