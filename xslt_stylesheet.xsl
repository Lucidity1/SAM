<?xml version="1.0"?>
<!--Sample XSLT stylesheet written by Factiva for demonstration purposes only. -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<xsl:template match="/">
	<html>
		<head>
			<title>Factiva Select II (XML) - Full-text Profiled Article Display</title>
		</head>
		<body bgcolor="#FFFFFF" style="font-family:Verdana, Arial, Sans-Serif;font-size:12px;">
		<table width="100%" border="0" cellspacing="0" cellpadding="0">
		<tr valign="top">  
			<td><div align="right"><a href="http://www.factiva.com"><img src="images/factiva.gif" width="135" height="90" border="0"/></a></div></td>
		</tr>
		</table>
		
		<xsl:apply-templates select="DistDoc/MetadataPT/PubData/Logo"/>
		
		<p></p>

		<b><xsl:value-of select="DistDoc/ArchiveDoc/Article/HandL/Title/Headline/Para"/></b><br/>
			<xsl:value-of select="DistDoc/ArchiveDoc/Article/Byline"/><p></p>
			<xsl:value-of select="format-number(DistDoc/MetadataPT/DocData/Num/@value, '######')"/> words<br/>
			<xsl:apply-templates select="DistDoc/MetadataPT/DocData/Date[@fid='pd']/@value"/><br/>
			<i><b><xsl:value-of select="DistDoc/MetadataPT/PubData/SrcName"/></b></i><br/>
			<xsl:value-of select="DistDoc/ArchiveDoc/Article/HandL/Title/SectionName[@fid='se']"/><br/>
			<p></p>
											
		<xsl:apply-templates select="DistDoc/ArchiveDoc/Article/HandL/LeadPara"/>
		
		<xsl:apply-templates select="DistDoc/ArchiveDoc/Article/TailParas"/><p></p>
		
		&#169;&#160;<xsl:value-of select="DistDoc/ArchiveDoc/Article/Copyright"/>.<p></p>
		
		<xsl:apply-templates select="DistDoc/MetadataPT/CodeSets/CSet[@fid='re']"/><p></p>
		<xsl:apply-templates select="DistDoc/MetadataPT/CodeSets/CSet[@fid='ns']"/><p></p>
		<xsl:apply-templates select="DistDoc/MetadataPT/CodeSets/CSet[@fid='co']"/><p></p>
		<xsl:apply-templates select="DistDoc/MetadataPT/CodeSets/CSet[@fid='in']"/><p></p>
		<p></p><p></p>
			
		<xsl:value-of select="DistDoc/@an"/>
		<hr/>
		<table width="100%" border="0" cellspacing="0" cellpadding="0" valign="top" align="right">
		<tr valign="top">  
			<td>
			<div valign="bottom" align="center"><font color="#A1A1A1" size="1">&#169; 2002 Factiva, a Dow Jones Reuters Company.  All Rights Reserved.</font></div>
			</td>
		</tr>
		</table>
		</body>
	</html>
</xsl:template>


<xsl:template match="DistDoc/MetadataPT/PubData/Logo">

		<xsl:variable name="LogoLink" select="@link"/>
		<xsl:variable name="LogoImageFile" select="@img"/>
		<xsl:variable name="LogoURL" select="@src"/>
				
	<xsl:choose>
		<xsl:when test="@link"><a href="{$LogoLink}"><img src="{$LogoURL}/{$LogoImageFile}" border="0"></img></a></xsl:when>
		<xsl:otherwise>
			<img src="{$LogoURL}/{$LogoImageFile}" border="0"></img><br/>
		</xsl:otherwise>
	</xsl:choose>
</xsl:template>


<xsl:template match="DistDoc/MetadataPT/CodeSets/CSet[@fid='re']">
		<xsl:choose>
			<xsl:when test=". = ' ' "><xsl:text></xsl:text></xsl:when>
		<xsl:otherwise>
			<b><u>Regions:</u></b><br/>
			<xsl:for-each select="Code/CodeD">
				<xsl:sort select="normalize-space(.)"/>
				<xsl:value-of select="."/><br/>
			</xsl:for-each>
		</xsl:otherwise>
		</xsl:choose>
</xsl:template>

<xsl:template match="DistDoc/MetadataPT/CodeSets/CSet[@fid='ns']">
		<xsl:choose>
			<xsl:when test=". = ' ' "><xsl:text></xsl:text></xsl:when>
		<xsl:otherwise>
			<b><u>News Subjects:</u></b><br/>
			<xsl:for-each select="Code/CodeD">
				<xsl:sort select="normalize-space(.)"/>
				<xsl:value-of select="."/><br/>
			</xsl:for-each>
		</xsl:otherwise>
		</xsl:choose>
</xsl:template>

<xsl:template match="DistDoc/MetadataPT/CodeSets/CSet[@fid='in']">
		<xsl:choose>
			<xsl:when test=". = ' ' "><xsl:text></xsl:text></xsl:when>
		<xsl:otherwise>
			<b><u>Industries:</u></b><br/>
			<xsl:for-each select="Code/CodeD">
				<xsl:sort select="normalize-space(.)"/>
				<xsl:value-of select="."/><br/>
			</xsl:for-each>
		</xsl:otherwise>
		</xsl:choose>
</xsl:template>

<xsl:template match="DistDoc/MetadataPT/CodeSets/CSet[@fid='co']">
		<xsl:choose>
			<xsl:when test=". = ' ' "><xsl:text></xsl:text></xsl:when>
		<xsl:otherwise>
			<b><u>Companies:</u></b><br/>
			<xsl:for-each select="Code/CodeD">
				<xsl:sort select="normalize-space(.)"/>
				<xsl:value-of select="."/><br/>
			</xsl:for-each>
		</xsl:otherwise>
		</xsl:choose>
</xsl:template>

<xsl:template match="DistDoc/ArchiveDoc/Article/HandL/LeadPara">
			<xsl:for-each select="Para">
			<xsl:value-of select="."/><p></p>
			</xsl:for-each>
</xsl:template>

<xsl:template match="DistDoc/ArchiveDoc/Article/TailParas">
			<xsl:for-each select="Para">
			<xsl:value-of select="."/><p></p>
			</xsl:for-each>
</xsl:template>

<xsl:template match="DistDoc/MetadataPT/DocData/Date[@fid='pd']/@value">
	<date xmlns:data="data.uri" xsl:exclude-result-prefixes="data">
		<xsl:variable name="month" select="number(substring(.,5,2))"/>
		<xsl:value-of select="document('')/*/data:data/data:months/data:m[$month]"/>
		<xsl:text> </xsl:text>		
		<xsl:value-of select="format-number(substring(., 7, 2), '##')"/>
		<xsl:text>, </xsl:text>
		<xsl:value-of select="substring(., 1, 4)"/>
	</date>
</xsl:template>

<data xmlns="data.uri">
<months>
   <m>January</m><m>February</m><m>March</m><m>April</m>
   <m>May</m><m>June</m><m>July</m><m>August</m>
   <m>September</m><m>October</m><m>November</m><m>December</m>
</months>
</data>


</xsl:stylesheet>
