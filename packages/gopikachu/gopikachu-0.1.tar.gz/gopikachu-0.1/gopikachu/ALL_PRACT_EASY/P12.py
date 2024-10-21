PRACTICAL NO.12

Write the program for the following: 
a. Create a web application to demonstrate JS Bootstrap Button
CODE:
ASPX CODE:
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm4.aspx.cs" Inherits="WebApplication8.WebForm4" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            position: absolute;
            top: 18px;
            left: 447px;
            z-index: 1;
        }
        </style>
    <link href="~/Content/bootstrap.min.css" rel="stylesheet" />
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="Label1" runat="server" BorderStyle="Solid" CssClass="auto-style1" Font-Bold="True" Text="JS BOOTSTRAP BUTTON"></asp:Label>
           <div class="container">
           
               <asp:Button ID="Button1" runat="server" CssClass="btn btn-primary" Text="Primary Buttton" style="z-index: 1; position: absolute; top: 187px; left: 487px" OnClick="Button1_Click" />
               <asp:Button ID="Button2" runat="server" CssClass="btn btn-success" Text="Success Button " style="z-index: 1; position: absolute; top: 254px; left: 491px" OnClick="Button2_Click" />
               <asp:Button ID="Button3" runat="server" CssClass="btn btn-danger" Text="Danger Buttton" style="z-index: 1; position: absolute; top: 121px; left: 492px" OnClick="Button3_Click" />
               <asp:Button ID="Button5" runat="server" CssClass="btn btn-info" Text="Info Buttton" style="z-index: 1; position: absolute; top: 394px; left: 493px; width: 148px;" OnClick="Button5_Click" />
           </div>
               <asp:Button ID="Button4" runat="server" CssClass="btn btn-warning" Text="Warning Button" style="z-index: 1; position: absolute; top: 327px; left: 496px" OnClick="Button4_Click" />

            </div>
    </form>
    </body>
</html>

C# CODE:
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication8
{
    public partial class WebForm4 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void Button3_Click(object sender, EventArgs e)
        {
            Response.Redirect("WebForm2.aspx");
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            Response.Redirect("WebForm3.aspx");
        }
        protected void Button2_Click(object sender, EventArgs e)
        {
            Response.Redirect("WebForm2.aspx");
        }
        protected void Button4_Click(object sender, EventArgs e)
        {
            Response.Redirect("WebForm3.aspx");
        }
        protected void Button5_Click(object sender, EventArgs e)
        {
            Response.Redirect("WebForm2.aspx");
        }
    }
}
OUTPUT:



b. Create a web application to demonstrate use of various Ajax controls.
CODE:
ASPX CODE:
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm5.aspx.cs" Inherits="WebApplication8.WebForm5" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Label ID="Label1" runat="server" BorderStyle="Solid" CssClass="auto-style1" Font-Bold="True" Text="AJAX CONTOLS"></asp:Label>
        </div>
        <asp:UpdatePanel ID="UpdatePanel1" runat="server">
            <ContentTemplate>
                <asp:ScriptManager ID="ScriptManager1" runat="server">
                </asp:ScriptManager>
                <asp:ScriptManagerProxy ID="ScriptManagerProxy1" runat="server"></asp:ScriptManagerProxy>
                <br />
                <br />
                Enter 1st Number :<asp:TextBox ID="TextBox1" runat="server" CssClass="auto-style3"></asp:TextBox>
                <br />
                <br />
                Enter 2nd Number:<asp:TextBox ID="TextBox2" runat="server" CssClass="auto-style2"></asp:TextBox>
                <br />
                <br />
                <asp:UpdateProgress ID="UpdateProgress1" runat="server">
                    <ProgressTemplate>
                        Please Wait Here...
                    </ProgressTemplate>
                </asp:UpdateProgress>
                <br />
                <br />
                <br />
                <asp:Label ID="Label2" runat="server" CssClass="auto-style4"></asp:Label>
                <br />
                <br />
                <br />
                <br />
                <asp:Label ID="Label3" runat="server" CssClass="auto-style5"></asp:Label>
                <asp:Label ID="Label4" runat="server" CssClass="auto-style6"></asp:Label>
                <br />
                <br />
                <br />
                <asp:Label ID="Label5" runat="server" CssClass="auto-style7"></asp:Label>
                <br />

                <asp:Timer ID="Timer1" runat="server" Interval="5000" OnTick="Timer1_Tick">
                </asp:Timer>
                <br />
                <asp:Label ID="Label6" runat="server" CssClass="auto-style9" style="z-index: 1"></asp:Label>
                <br />
                <br />
                <asp:Button ID="Button1" runat="server" CssClass="auto-style8" OnClick="Button1_Click" Text="Calculate" />

            </ContentTemplate>
        </asp:UpdatePanel>
    </form>
</body>
</html>

C# CODE:
using System;
namespace WebApplication8
{
    public partial class WebForm5 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            System.Threading.Thread.Sleep(2000);
            double n1 = Convert.ToDouble(TextBox1.Text);
            double n2 = Convert.ToDouble(TextBox2.Text);
            double add = n1 + n2;
            double sub = n1 -n2;
            double mul = n1 *n2;
            double div = n1 / n2;
            Label2.Text = "Addition is " +add.ToString();
            Label3.Text = "Subtraction is " + sub.ToString();
            Label4.Text = "Multiplication is " + mul.ToString();
            Label5.Text = "Division is " + div.ToString();
        }

        protected void Timer1_Tick(object sender, EventArgs e)
        {
            Label6.Text = DateTime.Now.ToString("hh:mm:ss:tt");
        }
    }
}
OUTPUT:

































c. Create a web application to demonstrate Installation and use of NuGet package.
CODE:
ASPX CODE:
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm6.aspx.cs" Inherits="WebApplication5.WebForm6" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            position: absolute;
            top: 19px;
            left: 432px;
            z-index: 1;
            width: 167px;
            height: 28px;
        }
        .auto-style2 {
            z-index: 1;
            left: 121px;
            position: absolute;
            width: 126px;
            top: 373px;
        }
    </style>
     <link href="~/Content/bootstrap.min.css" rel="stylesheet" />
</head>
<body>
    <form id="form1" runat="server">
        <div>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DETAILS FORM</div>
        <asp:Label ID="Label2" runat="server" style="z-index: 1; left: 19px; top: 171px; position: absolute; width: 104px" Text="Gender :"></asp:Label>
        <asp:Label ID="Label3" runat="server" style="z-index: 1; left: 24px; top: 234px; position: absolute" Text="Hobbies :"></asp:Label>
        <asp:Label ID="Label4" runat="server" style="z-index: 1; left: 22px; top: 373px; position: absolute; width: 91px; right: 1294px" Text="Country :"></asp:Label>
        <asp:Button ID="submit" CssClass="btn btn-primary" runat="server" OnClick="submit_Click" style="z-index: 1; left: 103px; top: 451px; position: absolute; right: 1230px; height: 29px" Text="Submit" />
        <asp:Label ID="show" runat="server" style="z-index: 1; left: 578px; top: 174px; position: absolute; width: 313px; height: 223px"></asp:Label>
        <asp:CheckBoxList ID="hb" runat="server" style="z-index: 1; left: 136px; top: 234px; position: absolute; height: 28px; width: 96px">
            <asp:ListItem Value="1">Cycling</asp:ListItem>
            <asp:ListItem Value="2">Reading</asp:ListItem>
            <asp:ListItem Value="3">Writing</asp:ListItem>
            <asp:ListItem Value="4">None</asp:ListItem>
        </asp:CheckBoxList>
        <asp:DropDownList ID="cn" runat="server" CssClass="auto-style2">
            <asp:ListItem Value="1">India</asp:ListItem>
            <asp:ListItem Value="2">USA</asp:ListItem>
            <asp:ListItem Value="3">Japan</asp:ListItem>
            <asp:ListItem Value="4">Nepal</asp:ListItem>
        </asp:DropDownList>
        <asp:RadioButtonList ID="gen" runat="server" RepeatDirection="Horizontal" style="z-index: 1; left: 112px; top: 168px; position: absolute; height: 28px; width: 231px">
            <asp:ListItem Value="1">Male</asp:ListItem>
            <asp:ListItem Value="2">Female</asp:ListItem>
            <asp:ListItem Value="3">Other</asp:ListItem>
        </asp:RadioButtonList>
        <asp:TextBox ID="name" runat="server" style="z-index: 1; left: 116px; top: 110px; position: absolute"></asp:TextBox>
        <asp:Label ID="Label5" runat="server" BorderStyle="Solid" CssClass="auto-style1" Font-Bold="True" Text="NuGet Packages"></asp:Label>
    </form>
</body>
</html>

C# CODE:
using System;
namespace WebApplication5
{
    public partial class WebForm6 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void submit_Click(object sender, EventArgs e)
        {
            string s = "Name :" + name.Text + "<br/>" + "Gender :" + gen.SelectedItem + "<br/>" + "Hobbies :" + hb.SelectedItem + "<br/>" + "Country :" + cn.SelectedItem + "<br/>";
            show.Text = s;
        }
    }
}

OUTPUT:
Solution Explorer-(Manage NuGet Packages)



Browse(Search and Install NuGet Packages)




Use:
