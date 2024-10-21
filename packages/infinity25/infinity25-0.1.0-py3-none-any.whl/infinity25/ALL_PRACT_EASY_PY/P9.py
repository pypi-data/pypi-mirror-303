PRACTICAL NO.09
Write the program for the following: 
a. Create a web application to demonstrate the use of different types of Cookies. 
CODE:
ASPX CODE:
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm11.aspx.cs" Inherits="WebApplication5.WebForm11" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            position: absolute;top: 22px;left: 370px;z-index: 1;width:306px;height: 30px; 
}
        .auto-style2 {
            position: absolute; top: 127px;   left: 314px;  z-index: 1;  width: 155px;
        }
        .auto-style3 {
            position: absolute; top: 182px;  left: 303px;  z-index: 1; width: 90px;right: 850px;
        }
        .auto-style4 {
            position: absolute; top: 128px; left: 474px;z-index: 1;
        }
        .auto-style5 {
            position: absolute; top: 182px; left: 475px;z-index: 1;
        }
        .auto-style6 {
            position: absolute;top: 268px;left: 484px;z-index: 1; width: 119px;height: 42px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
     
            <asp:Label ID="Label1" runat="server" BorderStyle="Solid" CssClass="auto-style1" Font-Bold="True" Font-Size="Large" Text="COOKIES MANAGEMENT"></asp:Label>
        </div>
        <asp:Label ID="Label2" runat="server" CssClass="auto-style2" Text="Username :"></asp:Label>
        <asp:Label ID="Label3" runat="server" CssClass="auto-style3" Text="Password :"></asp:Label>
        <asp:TextBox ID="un" runat="server" CssClass="auto-style4" OnTextChanged="TextBox1_TextChanged"></asp:TextBox>
        <asp:TextBox ID="up" runat="server" CssClass="auto-style5"></asp:TextBox>
        <asp:Button ID="Button1" runat="server" BorderStyle="Groove" CssClass="auto-style6" OnClick="Button1_Click" Text="Login" />
    </form>
</body>
</html>

C# CODE:
using System;
using System.Web;
namespace WebApplication5
{
    public partial class WebForm11 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            HttpCookie obj = new HttpCookie("User");
            obj["Username"] = un.Text;
            obj["Password"] = up.Text;
            obj.Expires = DateTime.Now.AddSeconds(10);
            Response.Cookies.Add(obj);
            Response.Redirect("WebForm9.aspx");
        }
    }
}
ASPX CODE:(Redirect)
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm9.aspx.cs" Inherits="WebApplication5.WebForm9" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            position: absolute;
            top: 17px;
            left: 463px;
            z-index: 1;
            width: 180px;
        }
        .auto-style2 {
            position: absolute;
            top: 159px;
            left: 254px;
            z-index: 1;
            width: 312px;
            height: 74px;
        }
        .auto-style3 {
            position: absolute;
            top: 325px;
            left: 248px;
            z-index: 1;
            width: 412px;
            height: 72px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="Label1" runat="server" CssClass="auto-style1" Text="Cookie Management"></asp:Label>
        </div>
        <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Retrive" />
        <asp:Label ID="Label2" runat="server" CssClass="auto-style2"></asp:Label>
        <asp:Label ID="Label3" runat="server" CssClass="auto-style3"></asp:Label>
    </form>
</body>
</html>
C# CODE:
using System;
using System.Web;
namespace WebApplication5
{
    public partial class WebForm9 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            
            HttpCookie data = Request.Cookies["User"];
            String datax = data["Username"].ToString();
            String datax2 = data["Password"].ToString();
            if (data != null)
            {
                Label2.Text = "Username : " + datax + "<br>" + "Password : " + datax2;

            }
            else
            {
                Label3.Text = "Cookies are expired";
            }
        }
    }
}
OUTPUT:
Storing Cookie:




Retriving Cookie:


Expiring Cookie:







b. Create a web application to demonstrate Form Security and Windows Security with proper Authentication and Authorization properties. 
CODE:

ASPX CODE: 
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm12.aspx.cs" Inherits="WebApplication5.WebForm12" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            position: absolute;
            top: 26px;
            left: 456px;
            z-index: 1;
            width: 104px;
        }
        .auto-style2 {
            position: absolute;
            top: 142px;
            left: 342px;
            z-index: 1;
        }
        .auto-style3 {
            position: absolute;
            top: 211px;
            left: 343px;
            z-index: 1;
            width: 67px;
        }
        .auto-style4 {
            position: absolute;
            top: 142px;
            left: 458px;
            z-index: 1;
        }
        .auto-style5 {
            position: absolute;
            top: 211px;
            left: 459px;
            z-index: 1;
        }
        .auto-style6 {
            position: absolute;
            top: 173px;
            left: 673px;
            z-index: 1;
            width: 351px;
        }
        .auto-style7 {
            position: absolute;
            top: 305px;
            left: 463px;
            z-index: 1;
            width: 142px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="Label1" runat="server" CssClass="auto-style2" Text="Username:"></asp:Label>
            <asp:Label ID="Label2" runat="server" CssClass="auto-style3" Text="Password:"></asp:Label>
            <asp:Label ID="Label3" runat="server" BorderStyle="Solid" CssClass="auto-style1" Font-Bold="True" Font-Size="Larger" Text="Login"></asp:Label>
        </div>
        <asp:TextBox ID="TextBox1" runat="server" CssClass="auto-style4"></asp:TextBox>
        <asp:TextBox ID="TextBox2" runat="server" CssClass="auto-style5" TextMode="Password"></asp:TextBox>
        <asp:Label ID="Label4" runat="server" CssClass="auto-style6" Enabled="False"></asp:Label>
        <asp:Button ID="Button1" runat="server" CssClass="auto-style7" OnClick="Button1_Click" Text="Submit" />
    </form>
</body>
</html>

C#CODE:
using System;
using System.Web.Security;
namespace WebApplication5
{
    public partial class WebForm12 : System.Web.UI.Page
    {

        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            string uname = TextBox1.Text;
            string pass = TextBox2.Text;
            if (FormsAuthentication.Authenticate(uname, pass))
            {
                FormsAuthentication.RedirectFromLoginPage(uname, false);
            }
            else
            {
                Label4.Text = "Login Details are Invalid";
            }
        }
    }
}

Web.Config :
<?xml version="1.0" encoding="utf-8"?>
<!--
  For more information on how to configure your ASP.NET application, please visit
  https://go.microsoft.com/fwlink/?LinkId=169433
  -->
<configuration>
	<appSettings>
		<add key="ValidationSettings:UnobtrusiveValidationMode" value="None" />
	</appSettings>
  <system.web>
    <compilation debug="true" targetFramework="4.5" />
    <httpRuntime targetFramework="4.5" />
	  <authentication mode="Forms">
		  <forms loginUrl="WebForm12.aspx" defaultUrl="WebForm13.aspx">
			  <credentials passwordFormat="Clear">
				  <user name="Admin" password="The World"/>
				  <user name="Lucifer" password="King"/>
			  </credentials>
		  </forms>
	  </authentication>
	  <authorization>
		  <allow users="Admin"/>
		  <allow users="Lucifer"/>
		  <deny users="?"/>
	  </authorization>
  </system.web>
  <system.codedom>
    <compilers>
      <compiler language="c#;cs;csharp" extension=".cs" type="Microsoft.CodeDom.Providers.DotNetCompilerPlatform.CSharpCodeProvider, Microsoft.CodeDom.Providers.DotNetCompilerPlatform, Version=2.0.1.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" warningLevel="4" compilerOptions="/langversion:6 /nowarn:1659;1699;1701" />
      <compiler language="vb;vbs;visualbasic;vbscript" extension=".vb" type="Microsoft.CodeDom.Providers.DotNetCompilerPlatform.VBCodeProvider, Microsoft.CodeDom.Providers.DotNetCompilerPlatform, Version=2.0.1.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" warningLevel="4" compilerOptions="/langversion:14 /nowarn:41008 /define:_MYTYPE=\&quot;Web\&quot; /optionInfer+" />
    </compilers>
  </system.codedom>
</configuration>
OUTPUT:
Authentication  and Authorization:

















