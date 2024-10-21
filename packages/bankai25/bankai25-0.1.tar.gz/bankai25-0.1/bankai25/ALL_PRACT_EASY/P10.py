            PRACTICAL NO.08
Write the program for the following: 
a. Create a web application for inserting and deleting records from a database. (Using Execute
Non Query). 

CODE:
ASPX CODE:

<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm8.aspx.cs" Inherits="WebApplication5.WebForm8" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
        <asp:Label ID="Label1" runat="server" BorderStyle="Solid" Font-Bold="True" Font-Size="Larger" style="z-index: 1; left: 501px; top: 30px; position: absolute; width: 333px; height: 31px" Text="USER MANAGEMENT"></asp:Label>
       <br /><br />
        <br /><br />
        <br />
        <asp:Label ID="Label2" runat="server" BorderStyle="Solid" CssClass="auto-style4" Font-Bold="True" Text="Enter ID :"></asp:Label>
        <asp:TextBox ID="TextBox5" runat="server" CssClass="auto-style9" TextMode="Number"></asp:TextBox>
        <table align="center">
            <tr>
                <td class="auto-style6"><b>Name</b></td>
                 <td class="auto-style7"> <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>&nbsp;</td>
            </tr>
             <tr>
                <td><b>Age</b></td>
                <td class="auto-style1">
                    <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td><b>Department</b><asp:GridView ID="GridView1" runat="server" CellPadding="4" GridLines="None" style="z-index: 1; left: 412px; top: 383px; position: absolute; height: 180px; width: 330px" CssClass="auto-style2" ForeColor="#333333">
            <AlternatingRowStyle BackColor="White" />
            <EditRowStyle BackColor="#2461BF" />
            <FooterStyle BackColor="#507CD1" ForeColor="White" Font-Bold="True" />
            <HeaderStyle BackColor="#507CD1" Font-Bold="True" ForeColor="White" />
            <PagerStyle BackColor="#2461BF" ForeColor="White" HorizontalAlign="Center" />
            <RowStyle BackColor="#EFF3FB" />
            <SelectedRowStyle BackColor="#D1DDF1" Font-Bold="True" ForeColor="#333333" />
            <SortedAscendingCellStyle BackColor="#F5F7FB" />
            <SortedAscendingHeaderStyle BackColor="#6D95E1" />
            <SortedDescendingCellStyle BackColor="#E9EBEF" />
            <SortedDescendingHeaderStyle BackColor="#4870BE" />
        </asp:GridView>
                 </td>
                <td class="auto-style1">
                    <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td><b>MobileNo</b></td>
                <td class="auto-style1">
                    <asp:TextBox ID="TextBox4" runat="server"></asp:TextBox></td>
            </tr>
             <tr>
                <td>
                                        <asp:Button ID="insert" runat="server" Text="Insert" OnClick="insert_Click" BorderStyle="Solid" Font-Bold="True" CssClass="auto-style8" />&nbsp;</td>
                <td class="auto-style1">
                    &nbsp;</td>
            </tr>
        </table>
                    <asp:Button ID="delete" runat="server" Text="Delete" BorderStyle="Solid" CssClass="auto-style3" Font-Bold="True" OnClick="delete_Click" Width="149px" />  
    </form>
</body>
</html>


C# CODE:
using System;
using System.Data;
using System.Data.SqlClient;

namespace WebApplication5
{
    public partial class WebForm8 : System.Web.UI.Page
    {
        SqlConnection con = new SqlConnection(@"Data Source=KING\SQLEXPRESS;Initial 					Catalog=College; Integrated Security=True");
        protected void Page_Load(object sender, EventArgs e)
        {
            retrive();
        }

        protected void insert_Click(object sender, EventArgs e)
        {
           
            con.Open();
            SqlCommand cmd = new SqlCommand(@"insert into Users values(
           '"+TextBox1.Text+"','" + Convert.ToInt32(TextBox2.Text)+ "','" +TextBox3.Text+ "','" +TextBox4.Text + "')",con);
             cmd.ExecuteNonQuery(); 
            Response.Write("Record Inserted Successfully");
            retrive();
            con.Close();
        }

        public void retrive()
        {
        
            SqlCommand cmd = new SqlCommand("select *from Users", con);
            SqlDataAdapter d = new SqlDataAdapter(cmd);
            DataTable dt = new DataTable();
            d.Fill(dt);
            GridView1.DataSource = dt;
            GridView1.DataBind();
           
        }


        protected void delete_Click(object sender, EventArgs e)
        {
            con.Open();
            SqlCommand cmd = new SqlCommand(@"delete from Users where ID=" + Convert.ToInt32(TextBox5.Text),con);
            cmd.ExecuteNonQuery();
            Response.Write("Record Deleted Successfully");
            retrive();
            con.Close();
        }
    }
}
OUTPUT:


Insert:






Delete:














b. Create a web application for user defined exception handling
CODE:

ASPX CODE: 
<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm10.aspx.cs" Inherits="WebApplication5.WebForm10" %>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            position: absolute;
            top: 25px;
            left: 471px;
            z-index: 1;
            width: 304px;
        }
        .auto-style2 {
            position: absolute;
            top: 98px;
            left: 382px;
            z-index: 1;
            width: 226px;
        }
        .auto-style3 {
            position: absolute;
            top: 99px;
            left: 646px;
            z-index: 1;
        }
        .auto-style4 {
            position: absolute;
            top: 154px;
            left: 373px;
            z-index: 1;
        }
        .auto-style5 {
            position: absolute;
            top: 160px;
            left: 644px;
            z-index: 1;
        }
        .auto-style6 {
            position: absolute;
            top: 462px;
            left: 372px;
            z-index: 1;
            width: 450px;
            height: 44px;
        }
        .auto-style7 {
            position: absolute;
            top: 136px;
            left: 921px;
            z-index: 1;
            width: 286px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
        <asp:Label ID="Label1" runat="server" CssClass="auto-style1" Font-Bold="True" Font-Size="Larger" Text="Arithmetic Operations"></asp:Label>
        <asp:TextBox ID="TextBox1" runat="server" CssClass="auto-style3" TextMode="Number"></asp:TextBox>
        <p>
            <asp:Label ID="Label3" runat="server" CssClass="auto-style2" Font-Bold="True" Font-Size="Large" Text="Enter First Number :"></asp:Label>
        </p>
        <p>
            &nbsp;</p>
        <asp:Label ID="Label4" runat="server" CssClass="auto-style4" Font-Bold="True" Font-Overline="False" Font-Size="Large" Text="Enter Second Number :"></asp:Label>
        <asp:TextBox ID="TextBox2" runat="server" CssClass="auto-style5"></asp:TextBox>
        <br /> <br /> <br /> 
        <asp:Label ID="error" runat="server" CssClass="auto-style7"></asp:Label>
        <br /> <br /> <br /> <br /> <br /> <br />
        <center><table>
            <tr>
                <td>
                    <asp:Button ID="add" runat="server" Text="Addition" OnClick="Button1_Click" /></td>
                 <td>
                     <asp:Button ID="sub" runat="server" Text="Subtraction" OnClick="Button2_Click" /></td>
                 <td>
                     <asp:Button ID="multi" runat="server" Text="Multiplication" OnClick="Button3_Click" /></td>
                 <td>
                     <asp:Button ID="div" runat="server" Text="Division" OnClick="Button4_Click" style="width: 85px" /></td>
            </tr>
                </table></center>
        <asp:Label ID="show" runat="server" CssClass="auto-style6"></asp:Label>
    </form>
</body>
</html>

C# CODE:
using System;

namespace WebApplication5
{
    public class DivideByZeroException25:Exception
    {
      public  DivideByZeroException25()
        {       
        }
      public  DivideByZeroException25(string Message):base(Message)
        {
        }
    }
    public partial class WebForm10 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            int res;
            int n1 = Convert.ToInt32(TextBox1.Text);
            int n2 = Convert.ToInt32(TextBox2.Text);
            res = n1 + n2;
            show.Text = "The Addition is : " + res.ToString();
        }

        protected void Button2_Click(object sender, EventArgs e)
        {
            int res;
            int n1 = Convert.ToInt32(TextBox1.Text);
            int n2 = Convert.ToInt32(TextBox2.Text);
            res = n1 - n2;
            show.Text = "The Subtraction is : " + res.ToString();
        }

        protected void Button3_Click(object sender, EventArgs e)
        {
            int res;
            int n1 = Convert.ToInt32(TextBox1.Text);
            int n2 = Convert.ToInt32(TextBox2.Text);
            res = n1 * n2;
            show.Text = "The Multiplication is : " + res.ToString();
        }
        protected void Button4_Click(object sender, EventArgs e)
        {
            try
            {
                int n1 = Convert.ToInt32(TextBox1.Text);
                int n2 = Convert.ToInt32(TextBox2.Text);
                int a = DivisionOp(n1, n2);
                show.Text = "The Division is : " + a.ToString();
            }
            catch (DivideByZeroException25 ex)
            {
                show.Text = ex.Message.ToString();
            }
        }
        public int DivisionOp(int n,int d)
        {
            if (d == 0)
            {
                throw new DivideByZeroException25("Exception Occured : Division By Zero is Not Possible");
            }
            else
            {
               return (n/d);
            }
        }
    }
}
OUTPUT:

