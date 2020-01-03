from maintainer_site.models.maintainer_group import MaintainerGroup

if isinstance(MaintainerGroup.objects.get().contact_information.get().email_address, str):
    main_email=MaintainerGroup.objects.get().contact_information.get().email_address
else:
    main_email=''

if isinstance(MaintainerGroup.objects.get().contact_information.get().primary_phone_number, str):
    main_phone=MaintainerGroup.objects.get().contact_information.get().primary_phone_number
else:
    main_phone=''

try:
    facebook_link=MaintainerGroup.objects.get().social_information.get().links.get(site='fac').url
    facebook_site='Facebook'
except:
    facebook_link=''
    facebook_site=''

try:
    medium_link=MaintainerGroup.objects.get().social_information.get().links.get(site='med').url
    medium_site='Medium'
except:
    medium_link=''
    medium_site=''

try:
    instagram_link=MaintainerGroup.objects.get().social_information.get().links.get(site='ins').url
    instagram_site='Instagram'
except:
    instagram_link=''
    instagram_site=''



html_content = """
	<!DOCTYPE html>
	<html>
	<body style="align-items: center;
	height: auto;
	position: relative;
	width: 100%;
	font-weight: normal;
	font-family: Roboto;
	font-style: normal;">
	<div class='table top' style="width: 100%;
	position: relative;
	display: table;	background: #293B52;
	height: 60px;">
	<div class='row' style="vertical-align: middle;
	display: table-cell;
	padding: 1em 2rem;">
	<span class='title-left white' style="position: relative;
	color: #FFFFFF;
	padding: 0;font-size: 1.5rem;
	color: #FFFFFF;
	float: left;">Subject/Text</span>
	<div class='inline-table' style="position: relative;
	height: 1.5rem;
	float: right;
	display: inline-table;">
	<span class='title-right white' style="position: relative;
	color: #FFFFFF;
	padding: 0.15em 0;font-size: 0.9rem;
	display: table-cell;
	vertical-align: middle;"><a href='TargetURL/Text' style="color:#FFFFFF">TargetApp/Text</a></span>
	</div>
	</div>
	</div>

	<div class='table top-second' style="width: 100%;
	position: relative;
	display: table;height: 108px;
	background: #F8D16C;">
	<div class='row' style="vertical-align: middle;
	display: table-cell;
	padding: 0 2rem;">
	<div class='post' style="font-size: 1.1rem;
	color: #293B52;">Posted By: Sender/Text</div>
	<div class='post' style="font-size: 1.1rem;
	color: #293B52;">Posted On: Time/Text</div>
	</div>
	</div>
	<div class='table mid' style="width: 100%;
	position: relative;
	display: table;	height: auto;">
	<div class='row' style="vertical-align: middle;
	display: table-cell;
	padding: 0 2rem;">
	<div class="mail-body" style="padding: 3em 0;
	height: auto;
	font-size: 1rem;
	max-width: 1400px;">Body/Text</div></div>
	</div>

	<div class='table bottom' style="width: 100%;
	position: relative;
	display: table;	height: 156px;
	background: #293B52;
	font-size: 1.125rem;">
	<div class='row white' style="vertical-align: middle;
	display: table-cell;
	padding: 0 2rem;position: relative;
	color: #FFFFFF;
	padding: 0;">
	<div class='table bottom2' style="width: 100%;
	position: relative;
	display: table;	">
	<div class='row bottom3' style="vertical-align: middle;
	display: table-cell;
	padding: 0 2rem;">
	<div class='email' style="margin-top: 10px;
	margin-bottom: 10px;">Email: <a href="mailto:MaintainerMail/Text" style="color:white;">MaintainerMail/Text</a></div>

	<div class='phone' style="margin-top: 10px;
	margin-bottom: 10px;">Phone: MaintainerPhone/Text</div>
	<div class='follow' style="margin-top: 10px;
	margin-bottom: 10px;">Follow us on: <a href="FacebookLink/Text" style="color:#FFFFFF">FacebookSite/Text</a> <a href="MediumLink/Text" style="color:#FFFFFF">MediumSite/Text</a> <a href="InstagramLink/Text" style="color:#FFFFFF">InstagramSite/Text</a></div>
	</div>

	<div class='logo' style="position: relative;
	float: right;
	display: table-cell;
	vertical-align: middle;padding-right: 2rem"><!--<img src="data:image/svg+xml;base64, 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
	" style="width: 100px;
	height: 100px;"/>	--></div>
	</div>
	</div>


	</div>
	</body>
	</html>


""".replace("MaintainerMail/Text",main_email).replace("MaintainerPhone/Text", main_phone).replace("MaintainerEmail/Text", main_email).replace("FacebookLink/Text", facebook_link).replace("FacebookSite/Text", facebook_site).replace("MediumLink/Text", medium_link).replace("MediumSite/Text", medium_site).replace("InstagramLink/Text", instagram_link).replace("InstagramSite/Text", instagram_site)

html_content.replace("Posted", 'abc')
