                    PRACTICAL NO.07
Write the program for the following: 
a.Create Web Form to demonstrate use of Website Navigation controls.
CODE:
ASPX CODE:
1]Master Page:

<%@ Master Language="C#" AutoEventWireup="true" CodeBehind="Site1.master.cs" Inherits="WebApplication6.Site1" %>

<!DOCTYPE html>

<html>
<head runat="server">
    <title></title>
    <asp:ContentPlaceHolder ID="head" runat="server">
    </asp:ContentPlaceHolder>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:ContentPlaceHolder ID="ContentPlaceHolder1" runat="server">

            </asp:ContentPlaceHolder>
        </div>
       <center><h1>Website Navigation Controls</h1></center> <br />
        <h1>Menu :</h1><br />
        <asp:Menu ID="Menu1" runat="server" DataSourceID="SiteMapDataSource1">
        </asp:Menu>
        <br />
        <br />
   
        <asp:SiteMapDataSource ID="SiteMapDataSource1" runat="server" />
        <asp:SiteMapDataSource ID="SiteMapDataSource2" runat="server" />
        <h1> TreeView :</h1>
        
        <asp:TreeView ID="TreeView1" runat="server" DataSourceID="SiteMapDataSource2" Font-Bold="True" Font-Size="Larger" ImageSet="Faq" style="z-index: 1; left: 66px; top: 465px; position: absolute; height: 93px; width: 175px">
            <HoverNodeStyle Font-Underline="True" ForeColor="Purple" />
            <NodeStyle Font-Names="Tahoma" Font-Size="8pt" ForeColor="DarkBlue" HorizontalPadding="5px" NodeSpacing="0px" VerticalPadding="0px" />
            <ParentNodeStyle Font-Bold="False" />
            <SelectedNodeStyle Font-Underline="True" HorizontalPadding="0px" VerticalPadding="0px" />
        </asp:TreeView>
         <br /><br/>   <br />   <br/>   <br />  <br/>  <br />  <br/>  <br /> <br/>

        <h1>HyperLink :</h1>
        <h1>
            <asp:HyperLink ID="HyperLink1" runat="server" Font-Size="Large" NavigateUrl="~/WebForm2.aspx">Next Page</asp:HyperLink>
        </h1>
        <br /> <br/> <br /> <br/> <br /><br/>

        <h1>Linked Button :</h1>
        <asp:LinkButton ID="LinkButton1" runat="server" OnClick="LinkButton1_Click">GO TO LAST PAGE</asp:LinkButton>
       
    </form>
</body>
</html>


2]WebPage with master code(1,2,3):

<%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication6.WebForm1" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <p>
    This is Home Page</p>
</asp:Content>


<%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm2.aspx.cs" Inherits="WebApplication6.WebForm2" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <p>
    This is Registration Page</p>
</asp:Content>


<%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm3.aspx.cs" Inherits="WebApplication6.WebForm3" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <p>
    This is Login Page</p>
</asp:Content>


C# CODE:
using System;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication6
{
    public partial class Site1 : System.Web.UI.MasterPage
    {
        protected void Page_Load(object sender, EventArgs e)
        {  
        }
        protected void LinkButton1_Click(object sender, EventArgs e)
        {
            Response.Redirect("WebForm3.aspx");
        }
    }
}

SiteMap File:
<?xml version="1.0" encoding="utf-8" ?>
<siteMap xmlns="http://schemas.microsoft.com/AspNet/SiteMap-File-1.0" >
  <siteMapNode url="~/WebForm1.aspx" title="Home"  description="This is Home Page">
    <siteMapNode url="~/WebForm2.aspx" title="Registration"  description="This is Registration Page" />
    <siteMapNode url="~/WebForm3.aspx" title="Login"  description="This is Login Page" />
  </siteMapNode>
</siteMap>

OUTPUT:





























b. Create a web application to demonstrate use of Master Page and content page
CODE:
ASPX CODE:
1]Master Page:
//Name:Rohit Laxman Ghadi
<%@ Master Language="C#" AutoEventWireup="true" CodeBehind="Site1.master.cs" Inherits="WebApplication7.Site1" %>

<!DOCTYPE html>
<html>
<head runat="server">
    <title></title>
    <asp:ContentPlaceHolder ID="head" runat="server">

    </asp:ContentPlaceHolder>
</head>
<body>
    <form id="form1" runat="server">
        <div>
      <asp:Label ID="Label1" runat="server" BorderStyle="Solid" Font-Bold="True" Font-Size="Larger" style="z-index: 1; left: 593px; top: 22px; position: absolute; width: 202px; height: 33px; margin-bottom: 3px" Text="FEEDBACK" ForeColor="Blue"></asp:Label>
            <br /><br /><br />
    </div>
            <asp:ContentPlaceHolder ID="ContentPlaceHolder1" runat="server">

            </asp:ContentPlaceHolder>
        
        <p>
            &nbsp;</p>
        <asp:Label ID="Label3" runat="server" BorderStyle="Solid" Font-Bold="True" Font-Size="Larger" ForeColor="Red" style="z-index: 1; left: 603px; top: 276px; position: absolute; width: 182px;" Text="Thank You"></asp:Label>
    </form>
</body>
</html>

3]WebPage with master code(1,2):

1]
<%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication7.WebForm1" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <p>
    <asp:Label ID="Label4" runat="server" style="z-index: 1; left: 398px; top: 104px; position: absolute; width: 118px" Text="Name :"></asp:Label>
    <asp:TextBox ID="TextBox1" runat="server" style="z-index: 1; left: 547px; top: 102px; position: absolute" AutoPostBack="True"></asp:TextBox>
    <br />
</p>
<p>
    <asp:Label ID="Label5" runat="server" style="z-index: 1; left: 397px; top: 161px; position: absolute; width: 95px" Text="Feedback:"></asp:Label>
</p>
<asp:TextBox ID="TextBox2" runat="server" style="z-index: 1; left: 542px; top: 159px; position: absolute" AutoPostBack="True"></asp:TextBox>
<p>
    <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" style="z-index: 1; left: 593px; top: 205px; position: absolute" Text="Submit" />
</p>
<p>
    &nbsp;</p>
</asp:Content>

2]
<%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm2.aspx.cs" Inherits="WebApplication7.WebForm2" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
 
    <p>
        <asp:Label ID="Label5" runat="server" style="z-index: 1; left: 521px; top: 163px; position: absolute; width: 289px; height: 63px"></asp:Label>
    </p>
    <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" style="z-index: 1; left: 610px; top: 241px; position: absolute" Text="Retrive" />
    <p>
    </p>
</asp:Content>


C# CODE:
1]WebForm 1 :
using System;
namspace WebApplication7
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
 		
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            Session["name"] = TextBox1.Text;
            Session["feed"] = TextBox2.Text;
            Response.Redirect("WebForm2.aspx");

        }
    }
}

2]WebForm 2:
using System;
namespace WebApplication7
{
    public partial class WebForm2 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
                        Label5.Text = "Information " + "<br/>" + "Name : " + 	Session["name"].ToString() + "<br/>" + "Feedback : " + Session["feed"].ToString();
        }
    }
}
OUTPUT:









c. Create a web application to demonstrate various states of ASP.NET Pages.

CODE:
ASPX CODE:
1]Master Page:
//Name:Rohit Laxman Ghadi
<%@ Master Language="C#" AutoEventWireup="true" CodeBehind="Site1.master.cs" Inherits="WebApplication7.Site1" %>
<!DOCTYPE html>
<html>
<head runat="server">
    <title></title>
    <asp:ContentPlaceHolder ID="head" runat="server">
    </asp:ContentPlaceHolder>
</head>
<body>
    <form id="form1" runat="server">
        <div>
      <asp:Label ID="Label1" runat="server" BorderStyle="Solid" Font-Bold="True" Font-Size="Larger" style="z-index: 1; left: 602px; top: 26px; position: absolute; width: 117px; height: 33px; margin-bottom: 3px" Text="Welcome" ForeColor="Blue"></asp:Label>
            <br />
            <br />
            <br />
        </div>
            <asp:ContentPlaceHolder ID="ContentPlaceHolder1" runat="server">
            </asp:ContentPlaceHolder>        
        <p>
      <asp:Label ID="Label2" runat="server" BorderStyle="Solid" Font-Bold="True" Font-Size="Larger" style="z-index: 1; left: 602px; top: 26px; position: absolute; width: 117px; height: 33px; margin-bottom: 3px" Text="Welcome" ForeColor="Blue"></asp:Label>
        </p>
        <asp:Label ID="Label3" runat="server" BorderStyle="Solid" Font-Bold="True" Font-Size="Larger" ForeColor="Red" style="z-index: 1; left: 585px; top: 280px; position: absolute" Text="Thank You"></asp:Label>
    </form>
</body>
</html>

3]WebPage with master code(1,2,3):

1]
<%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication7.WebForm1" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <p>
    <asp:Label ID="Label4" runat="server" style="z-index: 1; left: 250px; top: 103px; position: absolute; width: 118px" Text="Name :"></asp:Label>
    <asp:TextBox ID="TextBox1" runat="server" style="z-index: 1; left: 355px; top: 99px; position: absolute" AutoPostBack="True"></asp:TextBox>
    <br />
</p>
<p>
    <asp:Label ID="Label5" runat="server" style="z-index: 1; left: 250px; top: 147px; position: absolute; width: 95px" Text="Id :"></asp:Label>
</p>
<asp:TextBox ID="TextBox2" runat="server" style="z-index: 1; left: 353px; top: 146px; position: absolute" AutoPostBack="True"></asp:TextBox>
    <asp:Button ID="Button2" runat="server" OnClick="Button2_Click" style="z-index: 1; left: 983px; top: 179px; position: absolute; width: 48px" Text="+" />
    <asp:TextBox ID="TextBox3" runat="server" style="z-index: 1; left: 932px; top: 117px; position: absolute"></asp:TextBox>
<p>
    <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" style="z-index: 1; left: 400px; top: 190px; position: absolute" Text="Submit" />
    <asp:Button ID="Button3" runat="server" OnClick="Button3_Click" style="z-index: 1; left: 1238px; top: 145px; position: absolute" Text="Next" />
    <asp:Label ID="Label6" runat="server" style="z-index: 1; left: 872px; top: 120px; position: absolute" Text="Count"></asp:Label>
</p>
</asp:Content>

2]
<%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm2.aspx.cs" Inherits="WebApplication7.WebForm2" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <p>
        <asp:Label ID="Label4" runat="server" Font-Size="Large" style="z-index: 1; left: 574px; top: 100px; position: absolute; width: 135px" Text="Session State"></asp:Label>
        <br /> </p><p>
   </p>
    <p>
        <asp:Label ID="Label5" runat="server" style="z-index: 1; left: 521px; top: 163px; position: absolute; width: 289px; height: 63px"></asp:Label>
    </p>
    <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" style="z-index: 1; left: 610px; top: 241px; position: absolute" Text="Retrive" />
    <p>
    </p>
</asp:Content>



3]
<%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm3.aspx.cs" Inherits="WebApplication7.WebForm3" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <p>
        <asp:Label ID="Label5" runat="server" style="z-index: 1; left: 578px; top: 102px; position: absolute; width: 154px" Text="Application State"></asp:Label>
        <br />
    </p>
    <asp:Label ID="Label4" runat="server" style="z-index: 1; left: 452px; top: 144px; position: absolute; width: 105px" Text="Count"></asp:Label>
    <asp:TextBox ID="TextBox1" runat="server" style="z-index: 1; left: 526px; top: 144px; position: absolute"></asp:TextBox>
    <p>
    </p>
    <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" style="z-index: 1; left: 583px; top: 210px; position: absolute; width: 55px" Text="+" />
    <p>
    </p>
    <p>
    </p>
</asp:Content><%@ Page Title="" Language="C#" MasterPageFile="~/Site1.Master" AutoEventWireup="true" CodeBehind="WebForm3.aspx.cs" Inherits="WebApplication7.WebForm3" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <p>
        <asp:Label ID="Label5" runat="server" style="z-index: 1; left: 578px; top: 102px; position: absolute; width: 154px" Text="Application State"></asp:Label>
        <br />
    </p>
    <asp:Label ID="Label4" runat="server" style="z-index: 1; left: 452px; top: 144px; position: absolute; width: 105px" Text="Count"></asp:Label>
    <asp:TextBox ID="TextBox1" runat="server" style="z-index: 1; left: 526px; top: 144px; position: absolute"></asp:TextBox>
    <p>
    </p>
    <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" style="z-index: 1; left: 583px; top: 210px; position: absolute; width: 55px" Text="+" />
    <p>
    </p>
    <p>
    </p>
</asp:Content>
C# CODE:
1]WebForm 1 :
using System;
namspace WebApplication7
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
 		string a= (string)(ViewState["Show"] = "This is View State".ToString());
            Label7.Text = a;
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            Session["uname"] = TextBox1.Text;
            Session["pass"] = TextBox2.Text;
            Response.Redirect("WebForm2.aspx");

        }
        protected void Button2_Click(object sender, EventArgs e)
        {
            if (Application["count"] == null)
            {
                Application["count"] = 1;
                TextBox3.Text = Application["count"].ToString();
            }
            else
            {
                int i = Convert.ToInt32(Application["count"]);
                Application["count"] = i+1;
                TextBox3.Text = Application["count"].ToString();
            }
        }

        protected void Button3_Click(object sender, EventArgs e)
        {
            Response.Redirect("WebForm3.aspx");
        }
    }
}

2]WebForm 2:
using System;
namespace WebApplication7
{
    public partial class WebForm2 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            Label5.Text = "Information " + "<br/>" + "Username : " + Session["uname"].ToString() 	+ "<br/>" + "Password : " + Session["pass"].ToString();
        }
    }
}
3] WebForm 3:
using System;

namespace WebApplication7
{
    public partial class WebForm3 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            TextBox1.Text = Application["count"].ToString();
        }
    }
}






OUTPUT:
View State and Session State:
Application State :














